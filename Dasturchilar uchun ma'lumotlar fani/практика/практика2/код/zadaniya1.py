import numpy as np

v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])
sum_vectors = v1 + v2
diff_vectors = v1 - v2
dot_product = np.dot(v1, v2)
cosine_similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("Вектор 1:", v1)
print("Вектор 2:", v2)
print("Сумма:", sum_vectors)
print("Разность:", diff_vectors)
print("Скалярное произведение:", dot_product)
print("Косинусное сходство:", cosine_similarity)