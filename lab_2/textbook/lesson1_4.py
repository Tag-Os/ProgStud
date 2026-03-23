import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 50)
y = x

plt.title('Линейная зависимость y = x')
plt.xLAB_el('x')
plt.yLAB_el('y')
plt.grid()
plt.plot(x, y, 'r--')

plt.show()