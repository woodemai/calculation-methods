from sympy import diff, lambdify, symbols, sin, tanh
import numpy as np

x = symbols('x')
y = x * (pow(np.e, 4.0 * sin(x)) - 1) - 2 * (tanh(x) + 8)


def derivative_function(x, y):
    derivative = diff(y, x)
    derivative2 = diff(derivative, x)
    df = lambdify(x, derivative, 'numpy')
    ddf = lambdify(x, derivative2, 'numpy')
    return df, ddf


def bisection_method(a, b, epsilon, f):
    while abs(b - a) > 2 * epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def chord_method(a, b, epsilon, f):
    fa = f(a)
    fb = f(b)
    x0 = a - (b - a) * fa / (fb - fa)
    fx0 = f(x0)
    while abs(fx0) > epsilon:
        if fx0 == 0:
            return x0
        elif fa * fx0 < 0:
            b, fb = x0, fx0
        else:
            a, fa = x0, fx0
        x0 = a - (b - a) * fa / (fb - fa)
    return x0


def newton_method(a, b, epsilon, f):
    df, ddf = derivative_function(x,y)

    x0 = b if f(b) * ddf(b) > 0 else a
    xn = x0
    while True:
        fxn = f(xn)
        if abs(fxn) < epsilon:
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            return None
        xn = xn - fxn / dfxn

