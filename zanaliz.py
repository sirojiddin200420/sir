import matplotlib.pyplot as plt

categories = ['Смартфоны', 'Ноутбуки', 'Планшеты', 'Наушники', 'Смарт-часы']
sales = [120, 85, 40, 150, 95]

colors = ['blue', 'green', 'orange', 'red', 'purple']

plt.bar(categories, sales, color=colors)

plt.title("Отчет по продажам за месяц")
plt.xlabel("Категории товаров")
plt.ylabel("Количество (ед.)")

plt.grid(axis='y', linestyle='--')
plt.savefig("sales_report.png")
plt.show()