import numpy as np


def gauss_seidel(A, b, eps, max_iter=1000, sm_eps=1e-10, max_val=1e20):
    n = len(A)
    x = np.zeros_like(b)

    for _ in range(max_iter):
        old_x = np.copy(x)
        for i in range(n):
            temp1 = np.dot(A[i, :i], x[:i])
            temp2 = np.dot(A[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - temp1 - temp2) / (A[i, i] + eps)
            print(x)
            if np.abs(x[i]) > max_val or sm_eps > np.abs(x[i]):
                raise ValueError("The method did not converge. The values are approaching infinity.")
        if np.sqrt(np.dot(x - old_x, x - old_x)) < eps:
            return x


A = np.array([[0.32, -0.42, 0.85],
              [0.63, -1.43, -0.58],
              [0.84, -2.23, -0.52]], dtype=float)
b = np.array([1.32, 0.44, 0.64], dtype=float)

solution = gauss_seidel(A, b, 1e-20)
print("Решение:", solution)
