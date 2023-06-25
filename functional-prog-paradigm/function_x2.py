'''A function that calculates the sum of the squares of the values in a list using the MapReduce approach.'''

from functools import reduce

def sum_of_squares(l):
    squares = [x *x for x in l] # use list comprehension for mapping
    return reduce(lambda a,b: a+b, squares)

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

#revised
from functools import reduce

def sum_of_squares(l):
    integers = [int(x) for x in l]
    squares = [x * x for x in integers]
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2',  '3']))

#revised for comment outs
from functools import reduce

def sum_of_squares(l):
    integers = [int(x) for x in l if x[0] != '#']
    squares = [x * x for x in integers]
    return reduce(lambda a, b: a + b, squares)

print(sum_of_squares(['1', '2', '#100', '3']))