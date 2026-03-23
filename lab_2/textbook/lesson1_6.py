import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y1 = x

y2 = [i**2 for i in x]

plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title('Зависимости: y1 = x, y2 = x^2')
plt.yLAB_el('y1', fontsize=14)
plt.grid(True)
plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.xLAB_el('x', fontsize=14)
plt.yLAB_el('y2', fontsize=14)
plt.grid(True)

plt.show()