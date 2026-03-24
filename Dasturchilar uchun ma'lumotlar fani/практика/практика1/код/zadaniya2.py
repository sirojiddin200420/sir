import matplotlib.pyplot as plt

days = ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
temp = [7,9,11,10,8,6,5]

plt.plot(days,temp,marker='o')
plt.xlabel("День недели")
plt.ylabel("Температура °C")
plt.title("Температура за неделю")
plt.grid(True)
plt.show()