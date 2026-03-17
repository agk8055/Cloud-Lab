import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 10, 12, 15, 19])
y = np.array([10, 13, 18, 22, 27, 31])

mean_x, mean_y = np.mean(x), np.mean(y)
m = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x)**2)
c = mean_y - m * mean_x
print(f"Linear Formula: Y = {m:.2f}X + {c:.2f}")
reg = m * x + c

plt.scatter(x, y, label="Points")
plt.plot(x, reg, color="green", label="Linear Regression")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()