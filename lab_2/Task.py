import numpy as np
import matplotlib.pyplot as plt
def f(x):
    x = np.asarray(x)
    result = np.zeros_like(x)
    mask1 = (x >= 0) & (x <= 1)
    result[mask1] = -np.cos(np.exp(x[mask1]))
    mask2 = (x > 1) & (x <= 2)
    result[mask2] = np.log(2 * x[mask2] + np.sin(x[mask2] ** 2))
    return result

x = np.linspace(0, 2, 1000)
y = f(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)', color='blue')
plt.grid(True, linestyle='--', alpha=0.7)

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

x0 = 1.5
y0 = f(x0)
f_prime_x0 = derivative(f, x0)

x_tangent = np.linspace(x0 - 0.5, x0 + 0.5, 100)
y_tangent = f_prime_x0 * (x_tangent - x0) + y0

plt.plot(x_tangent, y_tangent, label='Касательная в точке x = 1.5', color='red', linestyle='--')

plt.title('График функции f(x) и касательная в точке x = 1.5', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend()

plt.annotate(f'Точка касания: ({x0:.2f}, {y0:.2f})', xy=(x0, y0), xytext=(x0 + 0.1, y0 + 0.3),
            arrowprops=dict(arrowstyle='->', color='green'))
plt.show()
