import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def is_convex(points):
    """
    Проверка выпуклости полигона по знакам векторных произведений.
    """
    positive = 0
    negative = 0
    points_count = len(points)
    for i in range(points_count):
        p1 = points[i]
        p2 = points[(i + 1) % points_count]
        p3 = points[(i + 2) % points_count]
        cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        if cross_product > 0:
            positive += 1
        elif cross_product < 0:
            negative += 1
    return positive == 0 or negative == 0

def draw_polygon(points):
    """
    Рисование полигона и проверка его свойств.
    """
    polygon = Polygon(points, closed=True, fill=None, edgecolor='r')
    plt.figure()
    plt.gca().add_patch(polygon)
    plt.plot(*zip(*points), marker='o', color='r', ls='')
    plt.xlim(min([p[0] for p in points]) - 1, max([p[0] for p in points]) + 1)
    plt.ylim(min([p[1] for p in points]) - 1, max([p[1] for p in points]) + 1)
    plt.grid(True)
    plt.show()

    # Проверка выпуклости
    if is_convex(points):
        print("Полигон выпуклый")
    else:
        print("Полигон невыпуклый")

    # Здесь могла бы быть ваша функция проверки самопересечения

points = [(2, 4), (-5, -4), (3, 1), (4, 0), (0, 4)]
draw_polygon(points)
