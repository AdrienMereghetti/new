# -*- coding: utf-8 -*-

import redis
import pygame, sys, os, time
from pygame.locals import *

cx = redis.Redis()
pubsub = cx.pubsub()  
pubsub.subscribe(['c1'])

pygame.init()

exit = 0
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Angry')
screen = pygame.display.get_surface()
angryBird = pygame.image.load('./images/AngryBird.png')
background = pygame.image.load('./images/Background.png')
'''
while True:

    for m in pubsub.listen():
        x, y = 0, 0
        #x = cx.get('joyx')
        #y = cx.get('joyy')
        
        x = int((float(cx.get('joyx')) + 1) * 300)
        if x > 600:
            x = 600
        y = int((float(cx.get('joyy')) + 1) * 200)
        if y > 400:
            y = 400
        print x
    screen.blit(background, (0,0))
    screen.blit(angryBird, (x,y))
    pygame.display.update()
'''
while 1:
        
