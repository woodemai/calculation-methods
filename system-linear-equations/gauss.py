import numpy as np


def gauss_elimination(A, b):
    n = len(b)
    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск максимального элемента в столбце для выбора опорного элемента
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[max_index, i]):
                max_index = j
        # Обмен строк для выбора опорного элемента
        A[[i, max_index]] = A[[max_index, i]]
        b[[i, max_index]] = b[[max_index, i]]
        # Выполнение прямого хода
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            b[j] -= factor * b[i]
            A[j, i:] -= factor * A[i, i:]

    # Обратный ход метода Гаусса
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


def refine_solution(A, b, x0):
    # Вычисление невязки
    residual = b - np.dot(A, x0)
    # Решение системы для уточнения
    delta = np.linalg.solve(A, residual)
    # Уточнение корней
    x = x0 + delta
    return x


# Пример использования
A = np.array([[0.32, -0.42, 0.85],
              [0.63, -1.43, -0.58],
              [0.84, -2.23, -0.52]])
b = np.array([1.32, 0.44, 0.64])

# Решение методом Гаусса
x0 = gauss_elimination(A, b)
print("Приближенное решение методом Гаусса:", x0)

# Уточнение корней
x_refined = refine_solution(A, b, x0)
print("Уточненное решение:", x_refined)
