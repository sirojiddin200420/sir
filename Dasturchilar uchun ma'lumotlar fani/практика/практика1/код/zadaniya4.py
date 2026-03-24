import matplotlib.pyplot as plt

months = ["Янв","Фев","Мар","Апр","Май","Июн","Июл","Авг","Сен","Окт","Ноя","Дек"]

usd = [12400,12500,12600,12650,12700,12650,12800,12850,11900,12950,13000,13100]
eur = [13500,13600,13700,13800,13900,14000,14100,13200,14300,14700,14300,14600]
rub = [135,136,137,138,140,139,141,145,147,149,150,150]

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(months,usd)
plt.title("Курс доллара")

plt.subplot(3,1,2)
plt.plot(months,eur)
plt.title("Курс евро")

plt.subplot(3,1,3)
plt.plot(months,rub)
plt.title("Курс рубля")
plt.xlabel("Месяц")

plt.tight_layout()
plt.show()