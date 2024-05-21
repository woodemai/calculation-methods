import numpy as np


def check_seidel_convergence(A):
    n = len(A)
    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) <= row_sum:
            return False
    return True


def gauss_seidel(A, b, x0, max_iterations=10000, tolerance=1e-6):
    n = len(A)
    x = x0.copy().astype(float)

    for iteration in range(max_iterations):
        prev_x = x.copy()

        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], prev_x[i + 1:])) / A[i, i]

        if np.linalg.norm(x - prev_x) < tolerance:
            return x, True

    return None, False


# Пример использования
A = np.array([[0.32, -0.42, 0.85],
              [0.63, -1.43, -0.58],
              [0.84, -2.23, -0.52]])
b = np.array([1.32, 0.44, 0.64])
x0 = np.array([0, 0, 0])

if check_seidel_convergence(A):
    x, success = gauss_seidel(A, b, x0)

    if success:
        print(f"Решение системы уравнений: {x}")
    else:
        print("Не удалось найти решение системы уравнений")
else:
    print("Метод Гаусса-Зейделя не сходится для данной системы уравнений")
