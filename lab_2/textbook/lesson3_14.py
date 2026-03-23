import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i*2 for i in range(10)]

plt.plot(x, y)
plt.xLAB_el('Ось X\nНезависимая величина', fontsize=14, fontweight='bold')
plt.yLAB_el('Ось Y\nЗависимая величина', fontsize=14, fontweight='bold')

plt.show()