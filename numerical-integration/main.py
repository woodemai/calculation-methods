import timeit
from functools import partial

from sympy import symbols, diff, lambdify

x = symbols('x')
y = x / (x ** 5 + 1)


def derivative_function(x, y):
    derivative = diff(y, x)
    derivative2 = diff(derivative, x)
    df = lambdify(x, derivative, 'numpy')
    ddf = lambdify(x, derivative2, 'numpy')
    return df, ddf


def rectangle_method(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def measure_execution_time(func, *args, **kwargs):
    result = func(*args, **kwargs)
    partial_func = partial(func, *args, **kwargs)
    execution_time = timeit.timeit(partial_func, number=10)
    return execution_time, result


def f(x):
    return x / (x ** 5 + 1)


a = 0
b = 5
n = 100


def rectangular_rule_error(a, b, h, f_second_derivative):
    max_derivative = max(f_second_derivative(x) for x in range(a, b + 1))
    error = (b - a) * h ** 2 / 24 * max_derivative
    return error


execution_time, result = measure_execution_time(rectangle_method, f, a, b, n)
df, ddf = derivative_function(x, y)
error = rectangular_rule_error(a, b, (b - a) / n, ddf)
print(f"The integral of f from {a} to {b} is approximately {result}.")
print(f"The execution time was {execution_time} seconds.")
print(f"Error: {error}")
