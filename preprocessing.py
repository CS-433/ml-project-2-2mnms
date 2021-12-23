import pandas as pd
import numpy as np

DATA_PATH = '/content/drive/MyDrive/ML/Project 2/data/'
PROBE_DATA_10MIN_PATH = DATA_PATH + 'Erlenbach_probe_data10min.csv'
ION_CONCENTRATION_PATH = DATA_PATH + 'Erlenbach_ion_concentration.csv'


def read_ion_concentration_csv():
    """ read 'Erlenbach_ion_concentration.csv' and return the corresponding dataframe
    """
    return pd.read_csv(ION_CONCENTRATION_PATH, parse_dates=[0], infer_datetime_format=True)


def read_probe_data10min_csv():
    """ read 'Erlenbach_probe_data10min.csv' and return the corresponding dataframe
        with updated column names
    """
    # read csv
    df = pd.read_csv(PROBE_DATA_10MIN_PATH, parse_dates=[0], infer_datetime_format=True)

    # new columns names
    column_names = {'DATE_TIME_UTC+1': 'date', 'NS_mm/10min': 'precipitation', 'WT_dC': 'water_temperature',
                    'LF_uS/cm': 'water_electrical_conductivity',
                    'Qu_mm/10min': 'flow', 'Comments_WSLdata': 'comments_WSLdata',
                    'Turbidity - Clean value [FTUeq] (Limit:0.00-150.00)': 'turbidity',
                    'NO3-Neq - Clean value [mg/l] (Limit:0.00-15.00)': 'NO3-Neq',
                    'TOCeq - Clean value [mg/l] (Limit:0.00-20.00)': 'TOCeq',
                    'DOCeq - Clean value [mg/l] (Limit:0.00-15.00)': 'DOCeq',
                    'Dissolved Oxygen - Clean value [ppm] (Limit:0.00-25.00)': 'dissolved_oxygen',
                    'Temperature DO - Clean value [°C] (Limit:0.00-50.00)': 'temperature_DO',
                    'Conductivity - Clean value [uS/cm] (Limit:0.10-600000.00)': 'conductivity',
                    'Temperature EC - Clean value [°C] (Limit:-20.00-130.00)': "temperature_EC",
                    'pH - Clean value (Limit:0.00-14.00)': 'pH',
                    'ORP - Clean value [mV] (Limit:-2000.00-2000.00)': 'ORP', 'Comments_SCANdata': 'comments_SCANdata'
                    }

    # rename columns
    df.rename(columns=column_names, inplace=True)

    return df


def prepare_ion_concentration_dataframe(ion_concentration):
    """do all preprocessing steps on the outputs, i.e. the ion_concentration dataframe"""
    remove_duplicates(ion_concentration)
    index_by_date(ion_concentration)
    remove_ion_outliers(ion_concentration)
    #extend_by_time_of_day_and_year(ion_concentration)

def prepare_probe_data10min_dataframe(probe_data10min):
    """do all preprocessing steps on the features, i.e. the probe_data10min dataframe"""
    skewed_columns = ['water_temperature', 'turbidity', 'TOCeq']

    remove_duplicates(probe_data10min)
    index_by_date(probe_data10min)
    log_transform(probe_data10min, skewed_columns)
    square_root_then_log_transform(probe_data10min, 'flow', c = 100)
    extend_by_time_of_day_and_year(probe_data10min)
    standardize(probe_data10min)

def remove_duplicates(df):
    """Remove duplicates from the data set""" 
    # drop pure duplications
    df.drop_duplicates(keep='first', inplace=True)

    # sort rows by number of nan vales
    df['count_nan'] = df.isna().sum(axis=1)

    # drop duplications according to date and keep the row with less nan values
    df = df.sort_values(by='count_nan').drop_duplicates(subset=['date'], keep='first') 

    df = df.drop(['count_nan'], axis=1)
    

def index_by_date(df):
    """Index the data by the date of the events"""
    df.set_index('date', inplace=True)
    df.sort_index(inplace=True)
    

def remove_ion_outliers(df):
    """Remove the outliers from the dataset"""
    # By observation on the data
    Na_MS_max = 2e4
    Mg_MS_max = 2e4
    K_MS_max =  1e4
    Ca_MS_max = 2e5

    outliers = df[(df['Na_MS'] >= Na_MS_max) |
                                 (df['Mg_MS'] >= Mg_MS_max) |
                                 (df['K_MS'] >= K_MS_max) |
                                 (df['Ca_MS'] >= Ca_MS_max)]

    df.drop(index=outliers.index, inplace=True)


def log_transform(df, columns):
    """ apply log transformation on the features of either ion_concentration or probe_data10min dataset"""
    for col in columns:
        df[col] = np.log10(1+df[col])


def square_root_then_log_transform(df, column, c = 100):
    """apply to a column x: x' = sqrt(x) * c (c is for getting larger values,
     well-suited for log transform) and then do the log transformation."""
    df[column] = np.sqrt(df[column]) * c
    df[column] = np.log(1 + df[column])

def extend_by_time_of_day_and_year(df):
    """create two additional features for the dataframe: time_of_year and time_of_day"""
    # day and year in terms of seconds
    day = 24 * 60 * 60
    year = day * 365.2425

    # dates casted in float
    dates_float = df.index.map(pd.Timestamp.timestamp)

    # set the two features
    df['time_of_day'] = np.sin(dates_float * 2 * np.pi / day)
    df['time_of_year'] = np.sin(dates_float * 2 * np.pi / year)


def standardize(df):
    """standardize each column/feature of the dataframe"""
    df = (df - df.mean()) / df.std()
