# import matplotlib.pyplot as plt

# names = ["A", "B", "C", "D"]
# values = [10, 20, 15, 25]

# plt.bar(names, values)
# plt.title("Bar chart")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(3)

# y1 = [10, 20, 15]
# y2 = [15, 25, 10]

# plt.bar(x - 0.2, y1, width=0.4)
# plt.bar(x + 0.2, y2, width=0.4)

# plt.xticks(x, ["A", "B", "C"])
# plt.title("Grouped bar chart")
# plt.show()

# import matplotlib.pyplot as plt

# x = ["A", "B", "C"]
# y1 = [10, 20, 15]
# y2 = [5, 10, 5]

# plt.bar(x, y1)
# plt.bar(x, y2, bottom=y1)

# plt.title("Stacked bar chart")
# plt.show()


import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

ax[0,0].plot([1,2,3],[1,4,9])
ax[0,1].bar(["A","B","C"],[3,5,2])
ax[1,0].scatter([1,2,3],[3,1,4])
ax[1,1].pie([30,40,30])

plt.show()