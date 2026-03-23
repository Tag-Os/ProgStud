import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]

plt.plot(x, y, LAB_el='steel price')
plt.title('Chart price', fontsize=15)
plt.xLAB_el('Day', fontsize=12, color='blue')
plt.yLAB_el('Price', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')

plt.show()