import matplotlib.pyplot as plt
import numpy as np

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
            root = method(a, a + epsilon, epsilon, f)  # Используйте метод бисекции
            roots.append(root)
        a += epsilon
    return roots


# Пример использования:
left = 0  # Левая граница отрезка
right = 8.0  # Правая граница отрезка
e = 1e-2  # Точность

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
plt.show()
# Приближенные корни на отрезке [0, 8.0]: [0.8665135000040798, 2.597829500009215, 6.617821500571122]