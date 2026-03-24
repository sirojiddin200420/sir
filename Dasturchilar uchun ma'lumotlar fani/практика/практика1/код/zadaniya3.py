import matplotlib.pyplot as plt

months = ["Янв","Фев","Мар","Апр","Май","Июн","Июл","Авг","Сен","Окт","Ноя","Дек"]
prices = [9200,9300,9100,9500,9600,9700,9800,9900,9950,10000,10100,10050]

plt.plot(months,prices,marker='o')
plt.xlabel("Месяц")
plt.ylabel("Цена бензина")
plt.title("Изменение цен на бензин за год")
plt.grid(True)
plt.show()