def bisection_method(a, b, epsilon, f, df):
    while abs(b - a) > 2 * epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def chord_method(a, b, epsilon, f, df):
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


def newton_method(a, b, epsilon, f, df):
    x0 = b if f(b) * df(b) > 0 else a
    xn = x0
    while True:
        fxn = f(xn)
        if abs(fxn) < epsilon:
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            print("Ноль производной. Нет решения.")
            return None
        xn = xn - fxn / dfxn
