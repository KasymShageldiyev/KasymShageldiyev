import numpy as np

# Направляющий вектор проектирования
vec_s = np.array([-3, 2, 1])

# Профильная проекция
if vec_s[0] == 0:
    print("Профильной проекции не существует, так как vec_s[0] = 0")
else:
    M_profile = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

# Фронтальная проекция
if vec_s[1] == 0:
    print("Фронтальной проекции не существует, так как vec_s[1] = 0")
else:
    M_frontal = np.array([[1, 0, 0],
                          [0, 0, 0],
                          [0, 0, 1]])

# Горизонтальная проекция
if vec_s[2] == 0:
    print("Горизонтальной проекции не существует, так как vec_s[2] = 0")
else:
    M_horizontal = np.array([[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 0]])

# Вывод матриц проектирования
print("Матрица профильной проекции:")
if 'M_profile' in locals():
    print(M_profile)
print("\nМатрица фронтальной проекции:")
if 'M_frontal' in locals():
    print(M_frontal)
print("\nМатрица горизонтальной проекции:")
if 'M_horizontal' in locals():
    print(M_horizontal)
