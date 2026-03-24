import matplotlib.pyplot as plt

days = ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
sleep = [6,5,6,5,7,9,8]

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(days,sleep,marker='o')
plt.title("Линейный график сна")

plt.subplot(3,1,2)
plt.bar(days,sleep)
plt.title("Столбчатая диаграмма сна")

plt.subplot(3,1,3)
plt.scatter(days,sleep)
plt.title("Точечная диаграмма сна")

plt.tight_layout()
plt.show()