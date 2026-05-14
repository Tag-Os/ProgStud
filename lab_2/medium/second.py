import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Гистограмма распределения', fontsize=14)
plt.xlabel('Значение', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.show()