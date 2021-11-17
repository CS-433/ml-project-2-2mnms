# variable names explained

## file Erlenbach_ion_concentration.csv

This file list the ion concentration measured from water samples. Missing values are indicated as NA. For Na, Mc, K and Ca, there are two measurements available (ion chromatrography and mass spectrometry). The ion chromatography is to be preferred, but mass spectrometry can be useful to fill some gaps.

- date is a datetime formatted as 2017-03-06T15:50:00Z in UTC+1
- Na, ..., SO4 are the ion concentrations measured through ion chromatography, in mg/l 
- Na_MS, Mg_MS, K_MS, Ca_MS are the ion concentrations measured through ICP mass spectrometry, in ug/l
- comments explain some possible NA and anomalous values

## file Erlenbach_probe_data10min.csv

This file includes quasi-continuous data measured from in-situ probes. The data comes from 2 main probe types, here called WSL and SCAN

### common to both probe types
DATE_TIME_UTC+1: date time formatted as 2017-03-06 17:20:00 in UTC+1

### data from WSL probe
NS_mm/10min: precipitation, measured in mm/10min
WT_dC: water temperature, measured in degrees Celsius
LF_uS/cm: water electrical conductivity, measured in uS/cm
Qu_mm/10min: flow, measured in mm/10min
Comments_WSLdata: string with comments

### data from SCAN probe
Turbidity - Clean value [FTUeq] (Limit:0.00-150.00):
NO3-Neq - Clean value [mg/l] (Limit:0.00-15.00):
TOCeq - Clean value [mg/l] (Limit:0.00-20.00):
DOCeq - Clean value [mg/l] (Limit:0.00-15.00):
Dissolved Oxygen - Clean value [ppm] (Limit:0.00-25.00):
Temperature DO - Clean value [°C] (Limit:0.00-50.00):
Conductivity - Clean value [uS/cm] (Limit:0.10-600000.00):
Temperature EC - Clean value [°C] (Limit:-20.00-130.00):
pH - Clean value (Limit:0.00-14.00):
ORP - Clean value [mV] (Limit:-2000.00-2000.00):
Comments_SCANdata:

### other derived data
dQ/dt: variation of discharge over the time interval