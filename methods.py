def bisection_method(a, b, epsilon, f):
    """
    Метод бисекции для нахождения корня уравнения f(x) = 0.

    Args:
        a (float): Левая граница отрезка.
        b (float): Правая граница отрезка.
        epsilon (float): Точность (разница между текущим и точным значением корня).
        f: функция

    Returns:
        float: Приближенное значение корня.
    """
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
    """
    Метод пропорциональных частей (метод хорд) для нахождения корня уравнения f(x) = 0.

    Args:
        a (float): Левая граница отрезка.
        b (float): Правая граница отрезка.
        epsilon (float): Точность (разница между текущим и точным значением корня).
        f: функция


    Returns:
        float: Приближенное значение корня.
    """
    while abs(b - a) > epsilon:
        x0 = a - (b - a) * f(a) / (f(b) - f(a))
        if f(x0) == 0:
            return x0
        elif f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0
    return (a + b) / 2
