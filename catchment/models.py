"""Module containing models representing catchment data.

The Model layer is responsible for the 'business logic' part of the software.

Catchment data is held in a Pandas dataframe (2D array) where each column contains
data for a single measurement site, and each row represents a single measurement
time across all sites.
"""

import pandas as pd


# If the class inherits from another class,
#  we include the parent class name in brackets.

# implementing the collection of measurement 
# sets as a dictionary with a known set of keys
# in a new class that contains Pandas Series
'''Composition'''
class MeasurementSeries:
    def __init__(self, series, name, units):
        self.series = series
        self.name = name
        self.units = units
        self.series.name = self.name
    
    def add_measurement(self, data):
        self.series = pd.concat([self.series,data])
        self.series.name = self.name
    
    def __str__(self):
        if self.units:
            return f"{self.name} ({self.units})"
        else:
            return self.name
        
# If the class inherits from another class, we include 
# the parent class name in brackets.
"""Inheritance from from Site and MeasurementSeries """
class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
#a class representing a measurement site
#If class X inherits from (is a) class Y, 
# we say that Y is
#the superclass or parent class of X, 
# or X is a subclass of Y.
class Site(Location):
    """A measurement site in the study."""
    #dunder method
    def __init__(self,name):
        #inherits the behaviour from super class location
        super().__init__(name)
        self.measurements = {}

    def add_measurement(self, measurement_id, data, units=None):    
        if measurement_id in self.measurements.keys():
            self.measurements[measurement_id].add_measurement(data)
    
        else:
            self.measurements[measurement_id] = MeasurementSeries(data, measurement_id, units)
 
    #add a property method  which will return the last data point in 
    # each measurement series, combined into a single dataframe:
    @property
    def last_measurements(self):
        return pd.concat(
            [self.measurements[key].series[-1:] for key in self.measurements.keys()],
            axis=1).sort_index()
    
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

