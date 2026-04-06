import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Education_Level": [1,2,1,3,2,3,1,2,3,2],
    "Working_Hours": [6,7,8,9,10,8,7,9,10,11],
    "Projects": [1,2,2,3,3,4,2,3,4,5],
    "Salary": [1000,1500,1800,2500,2700,3200,2000,3100,4000,4500]
}

df = pd.DataFrame(data)

# X va y
X = df.drop("Salary", axis=1)
y = df["Salary"]

# train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = LinearRegression()
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

# mse
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# koeffitsientlar
coeffs = pd.DataFrame(model.coef_, X.columns, columns=["Coefficient"])
print(coeffs)

print("Intercept:", model.intercept_)