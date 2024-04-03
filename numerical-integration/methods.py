from sympy import symbols, diff, lambdify

x = symbols('x')
y = 2 / (pow(x, 2 / 3) + pow(x, 1 / 3)) ** 2


def derivative_function(x, y):
    derivative = diff(y, x)
    derivative2 = diff(derivative, x)
    derivative3 = diff(derivative2, x)
    derivative4 = diff(derivative3, x)

    df1 = lambdify(x, derivative, 'numpy')
    df2 = lambdify(x, derivative2, 'numpy')
    df3 = lambdify(x, derivative3, 'numpy')
    df4 = lambdify(x, derivative4, 'numpy')

    return df1, df2, df3, df4


df1, df2, df3, df4 = derivative_function(x, y)


def rectangular_method_error(a, b, h, f_second_derivative):
    max_derivative = max(f_second_derivative(x) for x in range(a, b + 1))
    error = (b - a) * h ** 2 / 24 * max_derivative
    return error


def trapezoid_method_error(a, b, h, f_second_derivative):
    max_derivative = max(f_second_derivative(x) for x in range(a, b + 1))
    error = (b - a) * h ** 2 / 12 * max_derivative
    return error


def simpson_method_error(a, b, h, df4):
    max_df = max(df4(x) for x in range(a, b + 1))
    error = (b - a) * pow(h, 4) / 12 * max_df
    return error


def rectangle_method(f, a, b, n):
    h = (b - a) / n
    res = h * sum(f(a + i * h) for i in range(n))
    err = trapezoid_method_error(a, b, h, df2)
    return res, err


def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    res = h * (0.5 * f(a) + 0.5 * f(b) + sum(f(a + i * h) for i in range(1, n)))
    err = rectangular_method_error(a, b, h, df2)
    return res, err


def simpson_method(f, a, b, n):
    h = (b - a) / n
    res = h / 3 * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(
        f(a + i * h) for i in range(2, n, 2)))

    err = simpson_method_error(a, b, h, df4)
    return res, err
