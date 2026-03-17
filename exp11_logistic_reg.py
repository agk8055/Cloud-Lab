import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("iris.csv")
print(df.head())
#X=df.iloc[:,:-1]
#y=df.iloc[:,-1]
X=df[['sepal.length','sepal.width','petal.length','petal.width']]
y=df['variety']

label_encoder=LabelEncoder()
y=label_encoder.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy:.2f}")

s_len=float(input("Sepal Length: "))
s_wid=float(input("Sepal Width: "))
p_len=float(input("Petal Length: "))
p_wid=float(input("Petal Width: "))

sample = pd.DataFrame([[s_len, s_wid, p_len, p_wid]], columns=X.columns)
prediction=model.predict(sample)
species=label_encoder.inverse_transform(prediction)[0]
print(f"Predicted Species:{species}")