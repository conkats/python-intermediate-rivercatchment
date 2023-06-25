"""This is possible because Python treats functions as first-class objects that can 
be passed around as normal data. Here, we discuss decorators in more detail and learn how to write our own. """
def with_logging(func):

    """A decorator which adds logging to a function."""
    def inner(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return inner


def add_one(n):
    print("Adding one")
    return n + 1

# Redefine function add_one by wrapping it within with_logging function
add_one = with_logging(add_one)

# Another way to redefine a function - using a decorator
@with_logging
def add_two(n):
    print("Adding two")
    return n + 2

print(add_one(1))
print(add_two(1))

#for a decorator is measuring the time taken to execute a particular function.
#important for performance profiling
#Write a decorator which you can use to measure the execution time of the decorated function using the time.process_time_ns() function

import time

def profile(func):
    def inner(*args, **kwargs):
        start = time.process_time_ns()
        result = func(*args, **kwargs)
        stop = time.process_time_ns()

        print("Took {0} seconds".format((stop - start) / 1e9))
        return result

    return inner

@profile
def measure_me(n):
    total = 0
    for i in range(n):
        total += i*i
    return total


print(measure_me(1000000))