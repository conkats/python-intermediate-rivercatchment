# Functional style factorial function
def factorial_f(n):
    """Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n < 0:
        raise ValueError("Only use non-negative integers.")
    
    if n == 0 or n == 1:
        return 1 # exit from recursion, prevents infinite loops
    else:
        return  n * factorial_f(n-1) # recursive call to the same function

# Procedural style factorial function
def factorial(n):
    """Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n < 0:
        raise ValueError("Only use non-negative integers.")
    
    factorial = 1
    for i in range(1, n+1): #iterate from 1 to n
        # save intermediate value to use in the next iteration
        factorial = factorial * i 
    
    return factorial

print("Factorial of 6 using functional paradigm:",factorial(6))
print("Factorial of 6 using Procedural paradigm:", factorial_f(6))

name_lengths = map (len,["Mary", "Isla", "Sam"])
print(list(name_lengths))

#This is a mapping that squares every number in the passed 
# collection using anonymous, inlined lambda expression (a simple one-line mathematical expression representing a function):
# one-line lambda x, y, z, ...: expression code instead of defining and calling a named function f() as follows
#def f(x, y, z, ...):
#  return expression
squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print(list(squares))

## Don't do this
#add_one = lambda x: x + 1       

# Do this instead
#def add_one(x):
#  return x + 1

def add_one(num):
    return num + 1

result = map(add_one, [0, 1, 2])
print(list(result))

#Comprehension for Mapping/Data Generation
#list comprehension
integers = range(5)
double_ints = [2 * i for i in integers]
print(double_ints)

#using a map operation
integers = range(5)
double_ints = map(lambda i: 2 * i, integers )
print(list(double_ints))

#filter condition to the end
double_ints = [2 * i for i in integers if i % 2==0]
print(double_ints)

#Set and Dictionary Comprehensions and Generators
#Set
double_even_int_set = { 2*i  for i in integers if i % 2 ==0}
print(double_even_int_set)

#Dictionary
double_even_int_dict = {i: 2 * i for i in integers if i % 2 == 0}
print(double_even_int_dict)

#Generator expression- a type of an iterable object
double_generator = ( 2 * i for i in integers)
for x in double_generator:
    print(x)

#reducing
from functools import reduce
l = [1, 2, 3, 4]

def product(a, b):
    return a*b

print(reduce(product,l))
# The same reduction using a lambda function
print(reduce((lambda a, b: a * b), l))

#calculate the sequence of numbers
def add(a, b):
    return a + b

print(reduce(add,l))
# The same reduction using a lambda function
print(reduce((lambda a, b: a+b), l))


