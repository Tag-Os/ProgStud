import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Линейный график с seaborn
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.normal(0, 0.1, 50)

sns.set_theme(style="darkgrid")
sns.lineplot(x=x, y=y)

plt.title('Линейный график с seaborn')
plt.xlabel('x')
plt.ylabel('sin(x) + шум')

plt.show()