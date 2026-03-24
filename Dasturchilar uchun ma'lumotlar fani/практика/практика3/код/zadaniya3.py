import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9])
y = np.array([50, 55, 58, 60, 55, 70, 75, 90, 85, 90])

plt.figure()
plt.scatter(x, y)
plt.title("Задание 3: Часы подготовки и оценка")
plt.xlabel("Количество часов подготовки")
plt.ylabel("Оценка студента")
plt.grid()
plt.show()

print("Вывод: чем больше часов подготовки, тем выше оценка студента.")
print("На графике наблюдается положительная линейная зависимость.")