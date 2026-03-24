import numpy as np
import matplotlib.pyplot as plt

# Группа A
x_a = np.array([1, 2, 3, 4, 5])
y_a = np.array([60, 65, 70, 75, 80])

# Группа B
x_b = np.array([1, 2, 3, 4, 5])
y_b = np.array([50, 55, 60, 75, 70])

plt.figure()
plt.scatter(x_a, y_a, color='blue', label='Группа A')
plt.scatter(x_b, y_b, color='red', label='Группа B')
plt.title("Задание 4: Цветовое кодирование")
plt.xlabel("Количество часов подготовки")
plt.ylabel("Оценка")
plt.legend()
plt.grid()
plt.show()

print("Да, группы можно визуально отличить.")
print("Точки группы A расположены выше, чем точки группы B.")