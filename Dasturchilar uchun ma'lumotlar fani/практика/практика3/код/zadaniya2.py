import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 5, 4, 5, 7])

x_new = np.append(x, 4)
y_new = np.append(y, 15)

plt.figure()
plt.scatter(x_new, y_new)
plt.title("Задание 2: Выявление выброса")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

print("Добавлена точка (4, 15)")
print("Эта точка является выбросом, так как она сильно удалена от остальных точек.")
print("Она может исказить общий анализ данных и повлиять на корреляцию.")