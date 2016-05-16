import pygame
import random


# Человечки, legs 1-раздвинуть ноги, остальное сдвинуты
def draw_stick_figure(screen, x, y, color, legs):
    # Голова
    pygame.draw.ellipse(screen, (255, 228, 181), [1 + x, y, 10, 10], 0)
    # Ноги, 1-раздвинуты, остальное сдвинуты
    if (legs == 1):
        pygame.draw.line(screen, BLACK, [5 + x, 20 + y], [10 + x, 30 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 20 + y], [x, 27 + y], 2)
    else:
        pygame.draw.line(screen, BLACK, [5 + x, 20 + y], [5 + x, 30 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 20 + y], [5 + x, 30 + y], 2)
    # Тело
    pygame.draw.line(screen, color, [5 + x, 20 + y], [5 + x, 10 + y], 2)
    # Руки
    pygame.draw.line(screen, color, [5 + x, 10 + y], [9 + x, 20 + y], 2)
    pygame.draw.line(screen, color, [5 + x, 10 + y], [1 + x, 20 + y], 2)


# Мост
def bridge(screen, x, y):
    Color = (139, 69, 19)
    pygame.draw.line(screen, Color, [x, y], [360 + x, y], 5)
    xcoll = 0
    # Колонны
    while xcoll <= 360:
        pygame.draw.line(screen, Color, [xcoll, y], [xcoll, 50 + y], 5)
        xcoll += 40


# Корабль, x,y левая позиция 1 яруса
def sheep(screen, x, y):
    COLOR = (238, 99, 99)
    first_floor_height = 30
    second_floor_height = 20
    tube_height = 15
    roof_second_flor_y = y - first_floor_height - second_floor_height
    # Днище корабля
    pygame.draw.polygon(screen, COLOR, [[x, y], [240 + x, y], [200 + x, 50 + y], [x, 50 + y]], 0)
    # Первый ярус корабля
    pygame.draw.polygon(screen, COLOR, [[x + 20, y], [180 + x, y], [180 + x, y - first_floor_height],
                                        [20 + x, y - first_floor_height]], 0)
    # Второй ярус, который под трубами
    pygame.draw.polygon(screen, COLOR, [[x + 60, y - first_floor_height], [140 + x, y - first_floor_height],
                                        [140 + x, roof_second_flor_y], [60 + x, roof_second_flor_y]], 0)
    # Труба задняя
    pygame.draw.polygon(screen, COLOR, [[x + 80, roof_second_flor_y], [90 + x, roof_second_flor_y],
                                        [90 + x, roof_second_flor_y - tube_height],
                                        [80 + x, roof_second_flor_y - tube_height]], 0)
    # Труба передняя
    pygame.draw.polygon(screen, COLOR, [[x + 110, roof_second_flor_y], [120 + x, roof_second_flor_y],
                                        [120 + x, roof_second_flor_y - tube_height],
                                        [110 + x, roof_second_flor_y - tube_height]], 0)

    centre_y_porthole = y - int(first_floor_height / 2)
    r_porthole = int((first_floor_height - 10) / 2)
    # Элюминаторы слева направо
    pygame.draw.circle(screen, WHITE, [x + 40, centre_y_porthole], r_porthole, 0)
    pygame.draw.circle(screen, WHITE, [x + 70, centre_y_porthole], r_porthole, 0)
    pygame.draw.circle(screen, WHITE, [x + 130, centre_y_porthole], r_porthole, 0)
    pygame.draw.circle(screen, WHITE, [x + 160, centre_y_porthole], r_porthole, 0)


# Иницыализация дыма.
def create_smoke_sheep(x_left_tube, x_rigrt_tube, y, tube_width, tube_height, n):
    smoke_list = []
    # Задняя труба
    for i in range(n):
        y = random.randrange(y - tube_height, y)
        x = random.randrange(x_left_tube, x_left_tube + tube_width)
        smoke_list.append([x, y])
    # Передняя труба
    for i in range(n):
        y = random.randrange(y - tube_height, y)
        x = random.randrange(x_rigrt_tube, x_rigrt_tube + tube_width)
        smoke_list.append([x, y])
    return smoke_list


# Иницыализация людей.
def create_din_piople():
    people_list = []
    for i in range(10):
        x = random.randrange(0, 360)
        y = 450
        speed = random.randrange(1, 5)
        color = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
        legs = random.randrange(0, 1)
        people_list.append([x, y, speed, color, legs])
    return people_list


# Рисуем и меняем дым
def draw_and_change_smoke(screen, sm_list, rect_x, rect_y, rect_change_x):
    for i in range(len(sm_list)):
        pygame.draw.circle(screen, WHITE, sm_list[i], 4, 0)
        if (abs(sm_list[i][1] - rect_y) > 30):
            sm_list[i][1] = random.randrange(rect_y - 85, rect_y - 65)
            if i < len(sm_list) / 2:
                sm_list[i][0] = random.randrange(rect_x + 80, rect_x + 90)
            else:
                sm_list[i][0] = random.randrange(rect_x + 110, rect_x + 120)
        sm_list[i][0] += -1 * int(rect_change_x / 5) * random.randrange(1, 100)
        sm_list[i][1] += int(rect_change_x / 5)
    return sm_list


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (210, 105, 30)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1120, 700)
screen = pygame.display.set_mode(size)

background_image = pygame.image.load("2222.jpg").convert()
screen.blit(background_image, [0, 0])

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
# позиция динамического корабля
rect_x = 550
rect_y = 550
# Позиция статического корабля.
static_rect_x = 360
static_rect_y = 480
# Скорость и направление корабля
rect_change_x = 5
rect_change_y = 5
# Динамический дым и объекты
people_list = []
smoke_list = []

smoke_list = create_smoke_sheep(10000 + 110, 10000 + 80, 10000 - 65, 10, 20, 20)
people_list = create_din_piople()
smoke_list_static = create_smoke_sheep(static_rect_x + 110, static_rect_x + 80, static_rect_y - 65, 10, 20, 10)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image, [0, 0])

    # --- Drawing code should go here

    pygame.draw.polygon(screen, GREEN, [[0, 480], [180, 480], [180, 370], [0, 370]], 0)
    # pygame.draw.polygon(screen, WHITE, [[20, 440], [40, 440], [40, 400], [20, 400]], 0)
    m1 = 70
    m2 = 90
    pygame.draw.polygon(screen, WHITE, [[m1, 440], [m2, 440], [m1, 400], [m2, 400]], 0)
    m1 = 120
    m2 = 140
    pygame.draw.polygon(screen, WHITE, [[m1, 440], [m2, 440], [m1, 400], [m2, 400]], 0)
    m1 = 30
    m2 = 50
    pygame.draw.polygon(screen, WHITE, [[m1, 440], [m2, 440], [m1, 400], [m2, 400]], 0)
    bridge(screen, 0, 480)
    for i in range(len(people_list)):
        # Рисуем человечка
        draw_stick_figure(screen, people_list[i][0], people_list[i][1], people_list[i][3], people_list[i][4])
        # Изменяем позицию человечка на его скорость
        people_list[i][0] += people_list[i][2]
        if people_list[i][4] == 1:
            people_list[i][4] = 0
        else:
            people_list[i][4] = 1
        # Если человек дошел до конца моста
        if people_list[i][0] > 360:
            people_list[i][0] = 0
            people_list[i][1] = 450

    sheep(screen, static_rect_x, static_rect_y)
    smoke_list_static = draw_and_change_smoke(screen, smoke_list_static, static_rect_x, static_rect_y, 1)
    sheep(screen, rect_x, rect_y)
    smoke_list = draw_and_change_smoke(screen, smoke_list, rect_x, rect_y, rect_change_x)

    if rect_y > 650 or rect_y < 540:
        rect_change_y = rect_change_y * -1
    if rect_x > 1100:
        rect_x = -200
    rect_y += rect_change_y
    rect_x += rect_change_x

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)

# Close the window and quit.
pygame.quit()
