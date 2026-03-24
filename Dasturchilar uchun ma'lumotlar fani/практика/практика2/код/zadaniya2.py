import numpy as np
matrix = np.random.randint(1, 10, (4, 4))
transpose_matrix = matrix.T

det_matrix = np.linalg.det(matrix)

if det_matrix != 0:
    inverse_matrix = np.linalg.inv(matrix)
else:
    inverse_matrix = "Обратная матрица не существует"


if det_matrix == 0:
    singularity = "Матрица вырожденная"
else:
    singularity = "Матрица невырожденная"

print("Исходная матрица:\n", matrix)
print("Транспонированная матрица:\n", transpose_matrix)
print("Определитель:", det_matrix)
print("Обратная матрица:\n", inverse_matrix)
print(singularity)