import matplotlib.pyplot as plt

subjects = ["Математика","Python","Физика","История","Английский","Информатика"]
grades = [5,4,5,4,5,5]

plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
plt.plot(subjects,grades,marker='o')
plt.title("Линейный график оценок")

plt.subplot(2,1,2)
plt.bar(subjects,grades)
plt.title("Столбчатая диаграмма оценок")

plt.tight_layout()
plt.show()