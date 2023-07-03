import pandas as pd
import numpy as np

data = pd.DataFrame([[1., 2., 3.], [4., 5., 6.]],
                    index=['FP35','FP56']) #2x3
print(data)

location_measurement = [
    ("FP", "FP35", "Rainfall"),
    ("FP", "FP56", "River Level"),
    ("PL", "PL23", "River Level"),
    ("PL", "PL23", "Water pH")
]
index_names = ["Catchment", "Site", "Measurement"]
index = pd.MultiIndex.from_tuples(location_measurement,names=index_names)
data = [
    [0., 2., 1.],
    [30., 29., 34.],
    [34., 32., 33.],
    [7.8, 8., 7.9]
]

print(pd.DataFrame(data,index=index)) #shape 4x3

#use data structures to add an identifier to the measurements from
#each site
measurement_data = [
    {
        'site': 'FP35',
        'measurement': 'Rainfall',
        'data': [0.0, 2.0, 1.0],
    },
    {
        'site': 'FP56',
        'measurement': 'River level',
        'data': [30.0, 29.0, 34.0],
    },
]



#function to attach IDs to our measurement dataset
#use the range function to index into all three
#lists at the same location
def attach_information(data, sites, measurements):
     """Create datastructure containing data from a range of sites
       and instruments."""
     output = []

     for i in range(len(data)):
          output.append({'site': sites[i],
                         'measurement':measurements[i],
                         'data':data[i]})
     return output


data = np.array([[34., 32., 33.],
                 [7.8, 8.0, 7.9]])

output = attach_information(data, ['PL23', 'PL23'],
                            ['River Level', 'pH'])
print(output)

#fixing the issue of the above attach_information function
#if any of the arguments have different legnths
#and when looping, we run out of rows
#using the zip function,  which allows us to iterate 
#over multiple iterables without 
#needing an index variable.
def attach_names(data, sites, measurements):
     """Create datastructure containing measurement data from a range of sites."""
     assert len(data) == len(sites)
     assert len(data) == len(measurements)
     output = []

     for data_row, measurement, site in zip(data, measurements, sites):
          output.append({'site':site,
                         'measurement':measurement,
                         'data': data_row             
          })
     return output

output = attach_names(data, ['PL23', 'PL23'],
                            ['River Level', 'pH'])
print(output)

'''Classes'''
my_list = [1, 2, 3]
my_dict = {1: '1', 2: '2', 3: '3'}
my_set  = {1, 2, 3}

print(type(my_list))
print(type(my_dict))
print(type(my_set))

'''Encapsulationg Data'''
#from catchment.models import Site
#FP35 = Site('FP35')
#print(FP35.name)

'''Encapsulating behaviour'''
#from catchment.models import Site
#import datetime
#
#FP35 = Site('FP35')
#print(FP35)
#
#rainfall_data = pd.Series(
#    [0.0,2.0,1.0],
#    index=[
#        datetime.date(2000,1,1),
#        datetime.date(2000,1,2),
#        datetime.date(2000,1,3)
#        ]
#    )
#
#FP35.add_measurement('Rainfall',rainfall_data)
#
#print(FP35.measurements.keys())
#print(FP35.measurements['Rainfall'])

#Dunder Method
class Book:
    """A class to represent a book which has
     a title, an author and shows "title by author"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
         return self.title + ' by ' +self.author

book = Book('A Book', 'Me')

print(book)

#Composition
class Machine:
     pass

class Printer(Machine):
     pass

class Scanner(Machine):
     pass

class Copier(Printer, Scanner):
     #Copier `is a` Printer and `is a` Scanner
     pass

# vs inheritance
class Machine:
    pass

class Printer(Machine):
    pass

class Scanner(Machine):
    pass

class Copier(Machine):
    def __init__(self):
        # Copier `has a` Printer and `has a` Scanner
        self.printer = Printer()
        self.scanner = Scanner()