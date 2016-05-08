import pygame
import random

def draw_stick_figure(screen,x,y,color,legs):
    # Голова
    pygame.draw.ellipse(screen,(255,228,181),[1+x,y,10,10],0)
    # Ноги
    if(legs==1):
        pygame.draw.line(screen,BLACK,[5+x,20+y],[10+x,30+y],2)
        pygame.draw.line(screen,BLACK,[5+x,20+y],[x,27+y],2)
    else:
        pygame.draw.line(screen, BLACK, [5 + x, 20 + y], [5 + x, 30 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 20 + y], [5+x, 30 + y], 2)
    # Тело
    pygame.draw.line(screen,color,[5+x,20+y],[5+x,10+y],2)
    # Руки
    pygame.draw.line(screen,color,[5+x,10+y],[9+x,20+y],2)
    pygame.draw.line(screen,color,[5+x,10+y],[1+x,20+y],2)

def bridge(screen,x,y):
    Color=(139,69,19)
    pygame.draw.line(screen, Color, [ x,  y], [ 360 +x,  y], 5)
    xcoll=0
    while xcoll<=360:
        pygame.draw.line(screen, Color, [xcoll, y], [xcoll, 50+y], 5)
        xcoll+=40

def sheep(screen,x,y):
    Color = (139, 69, 19)
    k=30
    l=k+20
    pygame.draw.polygon(screen,Color,[[x,y],[240+x,y],[200+x,50+y],[x,50+y]],0)
    pygame.draw.polygon(screen, Color, [[x+20, y], [180 + x, y], [180 + x,  y-k], [20+x, y-k]], 0)
    pygame.draw.polygon(screen, Color, [[x + 60, y-k], [140 + x, y-k], [140 + x, y - l], [60 + x, y - l]], 0)
    pygame.draw.polygon(screen, Color, [[x + 80, y - l], [90 + x, y - l], [90 + x, y - l-15], [ 80+ x, y - l-15]], 0)
    pygame.draw.polygon(screen, Color, [[x + 110, y - l], [120 + x, y - l], [120 + x, y - l - 15], [110 + x, y - l - 15]],
                        0)




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
rect_x=500
rect_y=500
# Скорость и направление прямоугольника
rect_change_x = 5
rect_change_y = 5
people_list=[]
smoke_list=[]

for i in range(10):
    x = random.randrange(0, 360)
    y = 450
    speed=random.randrange(1,5)
    color=(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
    legs=random.randrange(0,1)
    people_list.append([x, y,speed,color,legs])

for i in range(10):
    y=random.randrange(rect_y-85,rect_y-65)
    x=random.randrange(rect_x+110,rect_x+120)
    smoke_list.append([x,y])
for i in range(10):
    y=random.randrange(rect_y-85,rect_y-65)
    x=random.randrange(rect_x+80,rect_x+90)
    smoke_list.append([x,y])


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
    #1120, 700
    sheep(screen,rect_x,rect_y)
    for i in range(len(smoke_list)):
        pygame.draw.circle(screen,WHITE,smoke_list[i],2,0)
        if(abs(smoke_list[i][0]-rect_x)>30):
            smoke_list[i][1]=random.randrange(rect_y-85,rect_y-65)
            if i<10:
                smoke_list[i][0]=random.randrange(rect_x+80,rect_x+90)
            else:
                smoke_list[i][0] = random.randrange(rect_x + 110, rect_x + 120)
        smoke_list[i][0] += int(rect_change_x/5)
        smoke_list[i][1] += int(rect_change_x/5)
                # Передвинуть исходную точку прямоугольника
    if rect_y > 650 or rect_y < 480:
        rect_change_y = rect_change_y * -1
    if rect_x > 1100-230 or rect_x < 370:
        rect_change_x = rect_change_x * -1
    rect_x += rect_change_x
    rect_y += rect_change_y


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()