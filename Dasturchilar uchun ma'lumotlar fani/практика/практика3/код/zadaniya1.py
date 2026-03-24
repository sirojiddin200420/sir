import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 5, 4, 5, 7])

plt.figure()
plt.scatter(x, y)
plt.title("Задание 1: Анализ корреляции")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

corr = np.corrcoef(x, y)[0, 1]
print("Коэффициент корреляции:", round(corr, 2))

if corr > 0.7:
    print("Зависимость сильная линейная.")
elif corr > 0.3:
    print("Зависимость умеренная линейная.")
elif corr > 0:
    print("Зависимость слабая линейная.")
else:
    print("Линейная зависимость отсутствует или очень слабая.")