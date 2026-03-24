import matplotlib.pyplot as plt

days = ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
steps = [8200,7100,7000,4800,8300,6200,5500]

plt.plot(days,steps,marker='o')
plt.xlabel("День")
plt.ylabel("Количество шагов")
plt.title("Количество шагов за неделю")
plt.grid(True)
plt.show()