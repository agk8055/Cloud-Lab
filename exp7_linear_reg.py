import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([5, 7, 10, 12, 15, 19]).reshape(-1, 1)
y = np.array([10, 13, 18, 22, 27, 31])

model = LinearRegression()
model.fit(x, y)
slope = model.coef_[0]
intercept = model.intercept_
predictions = model.predict(x)

print(f"Slope(m): {slope}")
print(f"Intercept(b): {intercept}")

plt.scatter(x, y, c='blue', label="Data points")
plt.plot(x, predictions, c="red", label="Linear Regression Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
