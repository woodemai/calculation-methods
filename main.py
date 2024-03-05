import matplotlib.pyplot as plt
import numpy as np
import time

from methods import bisection_method, chord_method


def f(x):
    return x * (pow(np.e, 4 * np.sin(x)) - 1) - 2 * (np.tanh(x) + 8)


def find_roots(a, b, epsilon, method):
    """
    Находит все корни уравнения f(x) = 0 на отрезке [a, b].

    Args:
        a (float): Левая граница отрезка.
        b (float): Правая граница отрезка.
        epsilon (float): Точность (разница между текущим и точным значением корня).
        method: метод для нахождения корней

    Returns:
        list: Список приближенных значений корней.
    """
    roots = []
    while a < b:
        if f(a) * f(a + epsilon) < 0:
            root = method(a, a + epsilon, epsilon, f)
            roots.append(root)
        a += epsilon
    return roots


start_time = time.time()
# Пример использования:
left = 0  # Левая граница отрезка
right = 8.0  # Правая граница отрезка
e = 1e-6  # Точность

all_roots = find_roots(left, right, e, chord_method)
print(f"Приближенные корни на отрезке [{left}, {right}]: {all_roots}")

# Определение области значений x
x = np.linspace(left - 1, right + 1, 100)

# Вычисление значений функции y = f(x)
y = f(x)

# Построение графика
plt.plot(x, y, label="f(x) = 𝑥(𝑒^4sin(𝑥) −1)−2(tanh(𝑥)+8)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("График функции f(x)")
plt.grid(True)
plt.legend()

end_time = time.time()
print(f'время выполнения {end_time - start_time}')

plt.show()
# Приближенные корни на отрезке [0, 8.0]: [0.866513143300948, 2.5978299242235683, 6.617821974427504]