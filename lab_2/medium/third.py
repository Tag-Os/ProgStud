import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n = 100
x = np.random.randn(n)
y = np.random.randn(n)
colors = np.random.choice(['red', 'green', 'blue'], n)

for color in ['red', 'green', 'blue']:
    mask = colors == color
    plt.scatter(x[mask], y[mask], label=f'Категория {color}', alpha=0.7, s=50)

plt.title('Диаграмма рассеяния', fontsize=14)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()