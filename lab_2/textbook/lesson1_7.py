import numpy as np
import matplotlib.pyplot as plt

fruits = ['apple', 'peach', 'orange', 'bannana', 'melon']
counts = [34, 25, 43, 31, 17]

plt.bar(fruits, counts)

plt.title('Fruits!')
plt.xLAB_el('Fruit')
plt.yLAB_el('Count')

plt.show()