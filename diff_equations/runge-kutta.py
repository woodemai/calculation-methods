import matplotlib.pyplot as plt
from math import  e

def runge_kutta_method(f, x0, y0, xn, n):
    """
    Runge-Kutta method for solving first order ordinary differential equation.

    Parameters:
    f (callable): Function describing the differential equation dy/dx = f(x, y)
    x0 (float): Initial value of the independent variable x
    y0 (float): Initial value of the dependent variable y
    xn (float): Final value of the independent variable x
    n (int): Number of steps

    Returns:
    x (list): List of values of the independent variable x
    y (list): List of corresponding values of the dependent variable y
    """
    h = (xn - x0) / n  # Step size
    x = [x0]
    y = [y0]

    for _ in range(n):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x[-1] + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x[-1] + h, y[-1] + k3)
        y_next = y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x[-1] + h
        x.append(x_next)
        y.append(float(y_next))

    return x, y


def f(x, y):
    return (2 * x - y * pow(e, x)) / pow(e, x)


x0 = 0  # Initial value of x
y0 = 0  # Initial value of y
xn = 10  # Final value of x
n = 1000  # Number of steps

x, y = runge_kutta_method(f, x0, y0, xn, n)

print("Values of x:")
print(x)
print("Values of y:")
print(y)

plt.figure(figsize=(10, 10))
plt.plot(x, y, label='Runge-Kutta method')
plt.title('Solution of the differential equation using Runge-Kutta method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
