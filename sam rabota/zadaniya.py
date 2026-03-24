import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ==========================================
# ЗАДАНИЕ 2. Данные (обучающая выборка)
# ==========================================

data = {
    "Area": [50, 70, 60, 90],
    "Rooms": [2, 3, 2, 4],
    "Floor": [3, 5, 2, 7],
    "Price": [120000, 180000, 150000, 250000]
}

df = pd.DataFrame(data)

# Признаки (X) и целевая переменная (y)
X = df[["Area", "Rooms", "Floor"]]
y = df["Price"]

# ==========================================
# ЗАДАНИЕ 3. Обучение модели
# ==========================================

model = LinearRegression()
model.fit(X, y)

# Прогноз для квартиры 80 м² (пример)
new_flat = pd.DataFrame([[80, 3, 5]], columns=["Area", "Rooms", "Floor"])
predicted_price = model.predict(new_flat)

print("Прогноз цены для квартиры 80 м²:", int(predicted_price[0]))

# ==========================================
# ЗАДАНИЕ 4. Оценка качества
# ==========================================

y_pred = model.predict(X)

mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("\nОценка модели:")
print("MAE:", mae)
print("R²:", r2)

# ==========================================
# Визуализация (дополнительно)
# ==========================================

plt.figure()
plt.scatter(df["Area"], y, label="Реальные данные")
plt.scatter(df["Area"], y_pred, label="Предсказания")
plt.xlabel("Площадь")
plt.ylabel("Цена")
plt.title("Регрессия: Площадь vs Цена")
plt.legend()
plt.grid()
plt.show()

# ==========================================
# Дополнительно: коэффициенты модели
# ==========================================

print("\nКоэффициенты модели:")
print("Area:", model.coef_[0])
print("Rooms:", model.coef_[1])
print("Floor:", model.coef_[2])
print("Свободный член:", model.intercept_)