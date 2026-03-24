import numpy as np
import matplotlib.pyplot as plt

subjects = ['Математика', 'Физика', 'Программирование', 'История']
group_A = [85, 78, 92, 88]
group_B = [79, 82, 85, 95]

x = np.arange(len(subjects))

width = 0.35

plt.bar(x - width/2, group_A, width, label='Группа А')
plt.bar(x + width/2, group_B, width, label='Группа Б')

plt.xlabel("Предметы")
plt.ylabel("Средний балл")
plt.title("Сравнение успеваемости студентов")

plt.xticks(x, subjects)

plt.legend()

plt.grid(axis='y', linestyle='--', alpha=0.6)


plt.show()