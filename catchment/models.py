"""Module containing models representing catchment data.

The Model layer is responsible for the 'business logic' part of the software.

Catchment data is held in a Pandas dataframe (2D array) where each column contains
data for a single measurement site, and each row represents a single measurement
time across all sites.
"""

import pandas as pd
import numpy as np


def read_variable_from_csv(filename):
    """Reads a named variable from a CSV file, and returns a
    pandas dataframe containing that variable. The CSV file must contain
    a column of dates, a column of site ID's, and (one or more) columns
    of data - only one of which will be read.

    :param filename: Filename of CSV to load
    :return: 2D array of given variable. Index will be dates,
             Columns will be the individual sites
    """
    dataset = pd.read_csv(filename, usecols=['Date', 'Site', 'Rainfall (mm)'])

    dataset = dataset.rename({'Date':'OldDate'}, axis='columns')
    #list comprehension
    dataset['Date'] = [pd.to_datetime(x,dayfirst=True) for x in dataset['OldDate']]
    dataset = dataset.drop('OldDate', axis='columns')

    newdataset = pd.DataFrame(index=dataset['Date'].unique())

    for site in dataset['Site'].unique():
        newdataset[site] = dataset[dataset['Site'] == site].set_index('Date')["Rainfall (mm)"]

    newdataset = newdataset.sort_index()

    return newdataset

def daily_total(data):
    """Calculate the daily total of a 2D data array.
    
    :param data: A 2D Pandas data frame with measurement data.
                 Index must be np.datetime64 compatible format. Columns are measurement sites.
    :returns: A 2D Pandas data frame with total values of the measurements for each day.
    """
    return data.groupby(data.index.date).sum()

def daily_mean(data):
    """Calculate the daily mean of a 2D data array.
    
    :param data: A 2D Pandas data frame with measurement data.
                 Index must be np.datetime64 compatible format. Columns are measurement sites.
    :returns: A 2D Pandas data frame with mean values of the measurements for each day.
    """
    return data.groupby(data.index.date).mean()


def daily_max(data):
    """Calculate the daily maximum of a 2D data array.

    :param data: A 2D Pandas data frame with measurement data. 
                 Index must be np.datetime64 compatible format. Columns are measurement sites.
    :returns: A 2D Pandas data frame with mean values of the measurements for each day.
    """
    return data.groupby(data.index.date).max()


def daily_min(data):
    """Calculate the daily min of a 2D data array.
    :param data: A 2D Pandas data frame with measurement data. 
                 Index must be np.datetime64 compatible format. Columns are measurement sites.
    :returns: A 2D Pandas data frame with mean values of the measurements for each day.
    """
    return data.groupby(data.index.date).min()

def data_normalise(data):
    """
    Normalise any given 2D data array
    
    NaN values are replaced with a value of 0
    
    :param data: 2D array of inflammation data
    :type data: ndarray

    """
    if not isinstance(data, np.ndarray) or not isinstance(data, pd.DataFrame):
        raise TypeError('data input should be DataFrame or ndarray')
    if len(data.shape) != 2:
        raise ValueError('data array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('Measurement values should be non-negative')
    max = np.nanmax(data, axis=0)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[np.newaxis, :]
    normalised[np.isnan(normalised)] = 0
    return normalised

def data_above_threshold(site_id, data, threshold):
    """Determine whether or not each data value exceeds a given threshold for a given site.

   :param site_id: The identifier for the site column
   :param data: A 2D Pandas data frame with measurement data. Columns are measurement sites.
   :param threshold: A threshold value to check against
   :returns: An integer representing the number of data points over a given threshold
    """
    #map(f, C) is a function that takes another function f() and a 
    #collection C of data items as inputs, applying the function f(x)
    from functools import reduce
    def count_above_threshold(a,b):
        if b:
            return a+1
        else:
            return a
    
    # Use map to determine if each daily inflammation value exceeds a given threshold for a patient
    above_threshold=  map(lambda x:x > threshold, data[site_id])

    # Use reduce to count on how many data points are above a threshold for a site
    return reduce(count_above_threshold, above_threshold, 0)