import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

x=np.array([[1],[2],[3],[4],[5],[6]])
y=np.array([2,5,7,9,10,14])

lin_model=LinearRegression()
dt_model=DecisionTreeRegressor(random_state=42)
rf_model=RandomForestRegressor(n_estimators=100,random_state=42)

lin_model.fit(x,y)
dt_model.fit(x,y)
rf_model.fit(x,y)

lin_pred=lin_model.predict(x)
dt_pred=dt_model.predict(x)
rf_pred=rf_model.predict(x)

lin_error=mean_squared_error(y,lin_pred)
dt_error=mean_squared_error(y,dt_pred)
rf_error=mean_squared_error(y,rf_pred)

print("Linear Regression Error: ",lin_error)
print("Decision Tree Error: ",dt_error)
print("Random Forest Error: ",rf_error)

errors={
"Linear Regression":lin_error,
"Decision Tree":dt_error,
"Random Forest":rf_error
}

best_model=min(errors,key=errors.get)
print("\nModel with minimum error:",best_model)
x_grid=np.arange(x.min(),x.max()+1,0.1).reshape(-1,1)
plt.scatter(x,y,label="Data")
plt.plot(x_grid,lin_model.predict(x_grid),label="Linear")
plt.plot(x_grid,dt_model.predict(x_grid),label="Decision Tree")
plt.plot(x_grid,rf_model.predict(x_grid),label="Random Forest")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Regression Model Comparison")
plt.show()