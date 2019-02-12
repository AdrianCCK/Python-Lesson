import pygame
import sys
from pygame.transform import flip
from Chef import Chef

    
       
       
pygame.init()

size = width, height = 640, 480
speed = [1, 0.5]
black = 0, 0, 0  #Red, Green, Blue
white = 255, 255, 255
red  = 255, 0, 0

screen = pygame.display.set_mode(size)


chef = Chef(width, height)
chefrect = chef.rect


for i in range(0,500):
    chef.y = chef.y + 1

    screen.fill(red)
    screen.blit(chef.image, chefrect)
    pygame.display.flip()
    print( i )

'''
t = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    if t % 4 == 0:
        #chefrect = chefrect.move(speed)
        chef.x = chef.x + 1
        #chef.y = chef.y + 1
    

    screen.fill(red)
    screen.blit(chef.image, chefrect)
    pygame.display.flip()
    t = t+1
    
    if t > 99999999:
      t = 0
'''
