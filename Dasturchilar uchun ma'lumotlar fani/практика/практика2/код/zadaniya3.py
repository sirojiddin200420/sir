import numpy as np

# Строки — объекты, столбцы — признаки: рост, вес, возраст
data = np.array([
    [170, 65, 20],
    [175, 70, 21],
    [168, 60, 19],
    [180, 75, 22],
    [172, 68, 20]
])

# 1. Среднее значение каждого признака
mean_values = np.mean(data, axis=0)

# 2. Нормализация признаков
normalized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# 3. Подматрица из первых трех объектов
submatrix = data[:3, :]

print("Матрица данных:\n", data)
print("Среднее значение каждого признака:", mean_values)
print("Нормализованные данные:\n", normalized_data)
print("Подматрица из первых трех объектов:\n", submatrix)