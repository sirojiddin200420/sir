import matplotlib.pyplot as plt

languages = ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'PHP']
share = [30, 18, 12, 25, 10, 5]

sorted_data = sorted(zip(share, languages), reverse=True)
share_sorted, languages_sorted = zip(*sorted_data)

colors = ['red' if lang == 'Python' else 'gray' for lang in languages_sorted]

bars = plt.barh(languages_sorted, share_sorted, color=colors)

for i, v in enumerate(share_sorted):
    plt.text(v + 1, i, f"{v}%", va='center')

plt.xlabel("Доля рынка (%)")
plt.ylabel("Языки программирования")
plt.title("Анализ рынка языков программирования")

plt.gca().invert_yaxis()

plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.show()