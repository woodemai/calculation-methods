import matplotlib.pyplot as plt
import numpy as np
import timeit

from functools import partial
from sympy import symbols, sin, tanh, diff, lambdify
from methods import bisection_method, chord_method, newton_method

# fill up with your data
left_border = 0
right_border = 8.0
epsilon = 1e-4
methods = [bisection_method, chord_method, newton_method]
x = symbols('x')
y = x * (pow(np.e, 4 * sin(x)) - 1) - 2 * (tanh(x) + 8)


def derivative_function(func):
    derivative = diff(func, x)
    return lambdify(x, derivative, 'numpy')


def f(x):
    return x * (pow(np.e, 4 * np.sin(x)) - 1) - 2 * (np.tanh(x) + 8)


df = derivative_function(y)


def find_roots(a, b, epsilon, method):
    roots = []
    while a < b:
        if f(a) * f(a + epsilon) < 0:
            root = method(a, a + epsilon, epsilon, f, df=df)
            roots.append(root)
        a += epsilon
    return roots


def show_graph(left, right):
    x = np.linspace(left, right, 1000)
    y = f(x)
    _, ax = plt.subplots()
    ax.plot(x, y, label="График функции")
    plt.grid(True)
    plt.legend()
    ax.axhline(y=0, color='black', linewidth=2)
    plt.show()


def run_methods():
    for method in methods:
        run_method(method, left_border, right_border, epsilon)


def run_method(method, left, right, epsilon):
    roots = find_roots(left, right, epsilon, method)
    partial_func = partial(find_roots, left, right, epsilon, method)
    execution_time = timeit.timeit(partial_func, number=5)
    print(f'Время выполнения с методом {str(method).split()[1]}: {execution_time}')
    print(f'Корни: {str(roots)}')


run_methods()
show_graph(left_border, right_border)
