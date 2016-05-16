import pygame
import random
import math

WHITE = (255, 255, 255)
rx = 10
ry = 10
z = 0


def create_smoke(x_tube, y, tube_width, tube_height, n):
    smoke_list = []
    # Задняя труба
    for i in range(n):
        y = random.randrange(y - tube_height, y)
        x = random.randrange(x_tube, x_tube + tube_width)
        smoke_list.append([x, y])
    return smoke_list


def draw_and_change(screen, sm_list, rect_x, rect_y, rect_change_x):
    for i in range(len(sm_list)):
        pygame.draw.circle(screen, WHITE, sm_list[i], 4, 0)
        if (abs(sm_list[i][1] - rect_y) > 30):
            sm_list[i][1] = random.randrange(rect_y - 85, rect_y - 65)
            if i < len(sm_list):
                sm_list[i][0] = random.randrange(rect_x + 80, rect_x + 90)
        sm_list[i][0] += -1 * int(rect_change_x / 5) * random.randrange(1, 100)
        sm_list[i][1] += int(rect_change_x / 5)
    return sm_list


def draw_car(xcar, ycar, dxcar):
    carcolor = (50, 50, 50)
    # cabine
    pygame.draw.polygon(screen, carcolor,
                        [[xcar - 120, ycar], [xcar - 120, ycar - 140], [xcar - 80, ycar - 180], [xcar, ycar - 180],
                         [xcar, ycar]], 0)
    # back
    pygame.draw.polygon(screen, carcolor,
                        [[xcar, ycar], [xcar + 250, ycar], [xcar + 250, ycar - 100], [xcar, ycar - 100]], 0)
    pygame.draw.polygon(screen, carcolor,
                        [[xcar - 120, ycar], [xcar - 120, ycar - 140], [xcar - 80, ycar - 180], [xcar, ycar - 180],
                         [xcar, ycar]], 0)
    # window
    pygame.draw.polygon(screen, (225, 225, 255),
                        [[xcar - 100, ycar - 80], [xcar - 100, ycar - 120], [xcar - 80, ycar - 140],
                         [xcar - 20, ycar - 140],
                         [xcar - 20, ycar - 80]], 0)
    # trube
    pygame.draw.polygon(screen, carcolor,
                        [[xcar, ycar - 100], [xcar + 30, ycar - 100], [xcar + 30, ycar - 200], [xcar, ycar - 200]], 0)


def kolec(x, y, z):
    pygame.draw.circle(screen, (255, 255, 255), [x - 60, y], 30, 0)
    pygame.draw.circle(screen, (0, 0, 0), [x - 60, y], 30, 5)
    # pygame.draw.line(screen,(0,0,0),[x-90,y+30],[x-30,y-30],2)
    k = random.randint(1, 6)
    if z > 25:
        z = -25
    i = z
    ry = math.sqrt(900 - i * i)
    pygame.draw.line(screen, (0, 0, 0), [x - 60 - i, y + ry], [x - 60 + i, y - ry], 1)
    pygame.draw.line(screen, (0, 0, 0), [x - 60 + i, y + ry], [x - 60 - i, y - ry], 1)
    z += 5
    global rx
    global ry

    if z > 2 and z < 5:
        rnd = random.randint(-4, 0)
        rx = (30 + rnd) * math.cos(k)
        ry = (30 + rnd) * math.sin(k)
        pygame.draw.line(screen, (0, 0, 0), [x - 60 - rx, y + ry], [x - 60 + rx, y - ry], 2)
        pygame.draw.line(screen, (0, 0, 0), [x - 60 + rx, y + ry], [x - 60 - rx, y - ry], 2)
        z = 0
    if z < 2:
        pygame.draw.line(screen, (0, 0, 0), [x - 60 - 30, y], [x - 60 + 30, y], 2)
        pygame.draw.line(screen, (0, 0, 0), [x - 60, y + 30], [x - 60, y - 30], 2)

    # pygame.draw.line(screen, (0, 0, 0), [x-60 - rx, y + ry], [x - 60+rx, y  -ry], 1)
    # pygame.draw.line(screen, (0, 0, 0), [x - 60 + rx, y + ry], [x - 60 -rx, y - ry], 1)
    return z


size = (1120, 700)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
y = 570
x = 300
dx = 6
sm_list = create_smoke(x, y - 200, 30, 30, 10)
rx = 10
ry = 10
z = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.polygon(screen, (200, 200, 200), [[0, 0], [0, 2000], [2000, 2000], [2000, 0]], 1500)
    pygame.draw.line(screen, (100, 100, 100), [0, 600], [1120, 600], 10)

    draw_car(x, y, dx)
    z = kolec(x, y, z)
    kolec(x + 250, y, z)
    sm_list = draw_and_change(screen, sm_list, x - 70, y - 150, -1 * dx)

    if x < 50:
        x = 1200
    x -= dx

    pygame.display.flip()

    clock.tick(15)

pygame.quit()
