import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i*2 for i in range(10)]
plt.plot(x, y)
plt.xLAB_el('Ось X')
plt.yLAB_el('Ось Y')

plt.show()