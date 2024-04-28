import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.path import Path

def check_points_in_polygon(polygon_points, points):
    """
    Функция для определения, лежат ли точки внутри или снаружи полигона.
    """
    polygon = Polygon(polygon_points, closed=True)
    path = Path(polygon_points)
    
    plt.figure()
    ax = plt.gca()
    ax.add_patch(polygon)
    polygon.set_facecolor('none')
    polygon.set_edgecolor('r')

    for point in points:
        inside = path.contains_point(point)
        plt.plot(*point, 'go' if inside else 'bo', markersize=10)
        print(f"Точка {point} лежит {'внутри' if inside else 'снаружи'} полигона.")

    plt.xlim(min([p[0] for p in polygon_points]) - 1, max([p[0] for p in polygon_points]) + 1)
    plt.ylim(min([p[1] for p in polygon_points]) - 1, max([p[1] for p in polygon_points]) + 1)
    plt.grid(True)
    plt.show()

polygon_points = [(2, 2), (3, -1), (1, 0), (-2, -3), (-3, 1), (0, 0)]
points = [(2, 0), (-1, 3)]

check_points_in_polygon(polygon_points, points)
