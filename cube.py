import pygame
import numpy as np
from math import *


def connect_points(i, j, points):
    pygame.draw.line(screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("cube shit")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100
circle_pos = [WIDTH/2, HEIGHT/2]

projected2d = np.zeros((3, 1))

#rotation matrix
angle = 0

points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))



projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

projected_points = [
    [n, n] for n in range(len(points))
]

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    #update shit

    #rotation math
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])

    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    angle += 0.01



    screen.fill(WHITE)
    #draw 

    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        projected2d = np.dot(projection_matrix, rotated2d)  # Update projected2d by adding the rotated point

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1
    #connect_points(0, 1, projected_points)
    #connect_points(1, 2, projected_points)
    #connect_points(2, 3, projected_points)
    #connect_points(3, 0, projected_points)
    
    #connect_points(4, 5, projected_points)
   #connect_points(5, 6, projected_points)
    #connect_points(6, 7, projected_points)
    #connect_points(7, 4, projected_points)

    #connect_points(0, 4, projected_points)
    #connect_points(1, 5, projected_points)
    #connect_points(2, 6, projected_points)
   #connect_points(3, 7, projected_points)

    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points)
        connect_points(p, (p+4), projected_points)

    pygame.display.update()