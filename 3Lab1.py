import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Заданные вершины тетраэдра
vertices = np.array([[0, 0, 0],
                      [1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])

# Углы поворота
alpha = -np.pi + np.arccos(1/8)
beta = -np.arccos(np.sqrt(8)/2)
gamma = 1

# Матрицы поворота
Rx = np.array([[1, 0, 0],
               [0, np.cos(alpha), -np.sin(alpha)],
               [0, np.sin(alpha), np.cos(alpha)])

Ry = np.array([[np.cos(beta), 0, np.sin(beta)],
               [0, 1, 0],
               [-np.sin(beta), 0, np.cos(beta)])

Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0],
               [np.sin(gamma), np.cos(gamma), 0],
               [0, 0, 1]])

R = Rx @ Ry @ Rz

# Поворот вершин тетраэдра
rotated_vertices = vertices @ R.T

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Отрисовка осей
ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

# Отрисовка тетраэдра
ax.scatter(rotated_vertices[:, 0], rotated_vertices[:, 1], rotated_vertices[:, 2], c='orange', s=100)
for i in range(len(vertices)):
    ax.text(rotated_vertices[i][0], rotated_vertices[i][1], rotated_vertices[i][2], f'({vertices[i][0]}, {vertices[i][1]}, {vertices[i][2]})')

plt.show()
