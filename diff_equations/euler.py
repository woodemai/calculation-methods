import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, xn, n):
    """
    Метод Эйлера для решения обыкновенного дифференциального уравнения первого порядка.

    Параметры:
    f (callable): Функция, описывающая дифференциальное уравнение dy/dx = f(x, y)
    x0 (float): Начальное значение независимой переменной x
    y0 (float): Начальное значение зависимой переменной y
    xn (float): Конечное значение независимой переменной x
    n (int): Количество шагов

    Возвращает:
    x (list): Список значений независимой переменной x
    y (list): Список соответствующих значений зависимой переменной y
    """
    h = (xn - x0) / n  # Шаг
    x = [x0]
    y = [y0]

    for _ in range(n):
        x_next = x[-1] + h
        y_next = y[-1] + h * f(x[-1], y[-1])
        x.append(x_next)
        y.append(float(y_next))

    return x, y


def f(x, y):
    return (2 * x - y * pow(np.e, x)) / pow(np.e, x)


x0 = 0  # Начальное значение x
y0 = 0  # Начальное значение y
xn = 10  # Конечное значение x
n = 1000  # Количество шагов

x, y = euler_method(f, x0, y0, xn, n)

print("Значения x:")
print(x)
print("Значения y:")
print(y)
plt.figure(figsize=(10, 10))
plt.plot(x, y, label='Euler method')
plt.title('Solution of the differential equation using Euler method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
