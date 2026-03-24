import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[10,12,11,15,14,18,17]

plt.plot(x,y,marker='o')
plt.xlabel("День")
plt.ylabel("Значение")
plt.title("Исправленный график")
plt.ylim(10,20)
plt.grid(True)
plt.show()

