import timeit
from functools import partial
from methods import rectangle_method, trapezoid_method, simpson_method


def f(x):
    return 2 / (pow(x, 2 / 3) + pow(x, 1 / 3)) ** 2


def measure_execution_time(func, *args, **kwargs):
    res, err = func(*args, **kwargs)
    partial_func = partial(func, *args, **kwargs)
    execution_time = timeit.timeit(partial_func, number=10)
    return execution_time, res, err


a = 1
b = 8
n = 1000
methods = [rectangle_method, trapezoid_method, simpson_method]

for method in methods:
    execution_time, res, err = measure_execution_time(method, f, a, b, n)
    print(f"The integral of f from {a} to {b} is approximately {res}.")
    print(f"The execution time was {execution_time} seconds.")
    print(f"Error: {err}")
    print('\n')
