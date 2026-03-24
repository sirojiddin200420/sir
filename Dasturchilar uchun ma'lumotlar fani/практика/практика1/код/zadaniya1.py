import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [i**2 for i in x]

plt.plot(x,y,marker='o')
plt.xlabel("x")
plt.ylabel("y = x^2")
plt.title("График функции y = x^2")
plt.grid(True)
plt.show()