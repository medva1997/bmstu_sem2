import pygame
import random
def draw_stick_figure(screen,x,y,color,legs):
    # Голова
    pygame.draw.ellipse(screen,BLACK,[1+x,y,10,10],0)
    # Ноги
    if(legs==1):
        pygame.draw.line(screen,BLACK,[5+x,17+y],[10+x,27+y],2)
        pygame.draw.line(screen,BLACK,[5+x,17+y],[x,27+y],2)
    else:
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 27 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5+x, 27 + y], 2)
    # Тело
    pygame.draw.line(screen,color,[5+x,17+y],[5+x,7+y],2)
    # Руки
    pygame.draw.line(screen,color,[5+x,7+y],[9+x,17+y],2)
    pygame.draw.line(screen,color,[5+x,7+y],[1+x,17+y],2)

def bridge(screen,x,y):
    pygame.draw.line(screen, BLACK, [ x,  y], [ 360 +x,  y], 5)
    xcoll=0
    while xcoll<=360:
        pygame.draw.line(screen, BLACK, [xcoll, y], [xcoll, 50+y], 5)
        xcoll+=40




# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1120, 700)
screen = pygame.display.set_mode(size)
background_image=pygame.image.load("2222.jpg").convert()
screen.blit(background_image, [0,0])

pygame.display.set_caption("My Game")


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
rect_x=50
rect_y=50
# Скорость и направление прямоугольника
rect_change_x = 5
rect_change_y = 5
people_list=[]

for i in range(10):
    x = random.randrange(0, 360)
    y = 450
    speed=random.randrange(1,5)
    color=(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
    legs=random.randrange(0,1)
    people_list.append([x, y,speed,color,legs])


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

    #pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    # Нарисовать красный прямоугольник внутри белого
    #pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
    #draw_stick_figure(screen,rect_x-20,rect_y-20)
    bridge(screen,0,480)


    for i in range(len(people_list)):
        # Рисуем человечка
        draw_stick_figure(screen, people_list[i][0], people_list[i][1],people_list[i][3],people_list[i][4])
        # Изменяем позицию человечка на его скорость
        people_list[i][0] += people_list[i][2]
        if people_list[i][4] ==1: people_list[i][4] =0
        else: people_list[i][4] =1
        # Если человек дошел до конца моста
        if people_list[i][0] > 360:
            people_list[i][0]=0
            people_list[i][1]=450


    # Передвинуть исходную точку прямоугольника
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    rect_x += rect_change_x
    rect_y += rect_change_y


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()