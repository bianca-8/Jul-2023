from pygame import *
import random

screen = display.set_mode((1000, 600))
init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

ballX = 500
ballY = 450
mX = mouse.get_pos()[0] #mouse X
clock = time.Clock()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    screen.fill((WHITE))
    draw.rect(screen, RED, (mX, 500, 100, 20)) #slide
    draw.circle(screen, BLACK, (ballX, ballY), 5)

    #if ballY == 500 and ballX >= mX and ballX <= mX + 100: #touching slide


    display.flip()
    clock.tick(60)

quit()