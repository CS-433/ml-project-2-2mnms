# Project 2 - Predicting Ions Concentration in Water Streams

Names : Berezantev Mihaela, Sinsoillier Mike Junior, Du Couédic De Kergoualer Sophie Zhuo Ran

## Background
This repository contains the code to produce two models dedicated to predict the ion concentrations in water streams using data measures from in-situ probes.

This repository contains:
* [Erlenbach_ion_concentration.csv](data/Erlenbach_ion_concentration.csv) : The ion concentrations sampled at different times (approximately every two hours). Represents the values to predict.
* [Erlenbach_probe_data10min.csv](data/Erlenbach_probe_data10min.csv) : Different low-cost data measures from in-situ probes. Used as the features for the models.
* [report.pdf](report.pdf) : the report explaining the complete process of this project
* [scripts](scripts/): all the executable code, in particular
  * [Data_preprocessing.ipynb](scripts/Data_preprocessing.ipynb): a notebook illustrating our procedure to preprocess the data
  * [Boosting_Regressor.ipynb](scripts/Boosting_Regressor.ipynb): predictions using boosting regressor
  * [NN.ipynb](scripts/NN.ipynb): predictions using a recursive neural network
  * [preprocessing.py](scripts/preprocessing.py): implementation of the functions actually used to preprocess the data

## Prequisites
The notebooks can be executed as they are in [Google Colaboratory](https://colab.research.google.com/?utm_source=scs-index). If you want to run them locally, make sure to have the following packages installed.
* [python3](https://www.python.org/downloads/). All the implementation are coded in python3.
* [pandas](https://pandas.pydata.org/docs/getting_started/install.html). Used for data exploration and preprocessing.
* [pytorch](https://pytorch.org/docs/stable/fft.html) were used to compute the fast Fourier transforms during features creation.
* [numpy](https://numpy.org/) : for an easy manipulations of the data arrays. You can install it via pip.
```bash
pip install numpy
```
* [scikit-learn](https://scikit-learn.org/stable/install.html) is a simple library for machine learning. Used both in the RNN and boosting regressor.
* [TensorFlow](https://www.tensorflow.org/install)
* [keras](https://pypi.org/project/keras/) is a deep learning API running with TensorFlow. It is necessary to run for the RNN.

## Usage
To run and produce the results made by the boosting regressor or the RNN, a folder with the path `/content/drive/MyDrive/ML/Project 2/data` should be created in google drive containing the two `.csv` files [Erlenbach_ion_concentration.csv](data/Erlenbach_ion_concentration.csv) and [Erlenbach_probe_data10min.csv](data/Erlenbach_probe_data10min.csv). The two notebooks can then simply be executed in Google Colaboratory.

If runned locally. The notebook should be updated with the appropriate paths to the data files, and the first cells of each notebook removed:
```python
from google.colab import drive
drive.mount('/content/drive')
```
