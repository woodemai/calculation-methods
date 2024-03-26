def rectangle_method(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    return h * (0.5 * f(a) + 0.5 * f(b) + sum(f(a + i * h) for i in range(1, n)))
