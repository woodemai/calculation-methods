import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import time

from methods import bisection_method, chord_method, newton_method


# fill up with your data
left_border = -100.0
right_border = 100.0
epsilon = 1e-5
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
    fig, ax = plt.subplots()
    ax.plot(x, y, label="График функции")
    plt.grid(True)
    plt.legend()
    ax.axhline(y=0, color='black', linewidth=2)
    plt.show()


def run_methods():
    for method in methods:
        run_method(method, left_border, right_border, epsilon)


def run_method(method, left, right, epsilon):
    start_time = time.time()
    roots = find_roots(left, right, epsilon, method)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Время выполнения с методом {str(method).split()[1]}: {execution_time}')
    print(f'Корни: {str(roots)}')
    show_graph(left, right)


run_methods()
