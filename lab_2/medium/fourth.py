import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.rand(5, 5)

plt.imshow(data, cmap='coolwarm', aspect='auto')
plt.colorbar(label='Значение')

for i in range(5):
    for j in range(5):
        plt.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center', 
                 color='white' if data[i, j] < 0.5 else 'black')

plt.title('Тепловая карта', fontsize=14)
plt.xticks(range(5), [f'X{i+1}' for i in range(5)])
plt.yticks(range(5), [f'Y{i+1}' for i in range(5)])
plt.show()