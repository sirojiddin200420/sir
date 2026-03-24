import numpy as np

# Создаем трехмерный тензор 3x4x5
tensor = np.arange(1, 61).reshape(3, 4, 5)

# 1. Сумма элементов по каждой оси
sum_axis0 = np.sum(tensor, axis=0)
sum_axis1 = np.sum(tensor, axis=1)
sum_axis2 = np.sum(tensor, axis=2)

# 2. Извлекаем двумерный срез
slice_2d = tensor[1, :, :]   # второй слой

# 3. Изменяем форму тензора в 6x10
reshaped_tensor = tensor.reshape(6, 10)

print("Исходный тензор:\n", tensor)
print("Сумма по оси 0:\n", sum_axis0)
print("Сумма по оси 1:\n", sum_axis1)
print("Сумма по оси 2:\n", sum_axis2)
print("Двумерный срез:\n", slice_2d)
print("Тензор размерности 6x10:\n", reshaped_tensor)