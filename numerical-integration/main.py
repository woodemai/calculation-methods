import timeit
from functools import partial
import numpy as np

def rectangle_method(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def measure_execution_time(func, *args, **kwargs):
    result = func(*args, **kwargs)
    partial_func = partial(func, *args, **kwargs)
    execution_time = timeit.timeit(partial_func, number=10)
    return execution_time, result


def f(x):
    return np.sin(x) * np.sinh(x)


a = 0
b = 1
n = 1000

execution_time, result = measure_execution_time(rectangle_method, f, a, b, n)
print(f"The integral of f from {a} to {b} is approximately {result}.")
print(f"The execution time was {execution_time} seconds.")












