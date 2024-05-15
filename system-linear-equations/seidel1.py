import numpy as np


def gauss_seidel(matrix, vector, max_iter=100, tol=1e-6):
    n = len(vector)
    x = np.zeros(n)

    x = np.linalg.solve(matrix, vector)

    for iter_count in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum_ax = np.dot(matrix[i, :i], x[:i]) + np.dot(matrix[i, i + 1:], x_old[i + 1:])
            x[i] = (vector[i] - sum_ax) / matrix[i, i]

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x

    print("Достигнуто максимальное количество итераций")
    return x


matrix = np.array([
    [0.34, 0.71, 0.63],
    [0.71, -0.65, -0.18],
    [1.17, -2.35, 0.75]
])
vector = np.array([2.08, 0.17, 1.28])

solution = gauss_seidel(matrix, vector, max_iter=1000, tol=0.0001)

print("Решение методом Гаусса-Зейделя:", solution)

check_equation = np.dot(matrix, solution) - vector
print("Подстановки решения:", check_equation)