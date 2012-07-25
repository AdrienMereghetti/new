# -*- coding: utf-8 -*-

import redis
import pygame, sys, os, time
from pygame.locals import *

cx = redis.Redis()
pubsub = cx.pubsub()  
pubsub.subscribe(['c1'])

pygame.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Angry')
screen = pygame.display.get_surface()

angryBird = pygame.image.load('./images/AngryBird.png')
angryBlackBird = pygame.image.load('./images/AngryBlackBird.png')
angryGreenBird = pygame.image.load('./images/AngryGreenBird.png')
angryPiggy = pygame.image.load('./images/AngryPiggy.png')
background = pygame.image.load('./images/Background2.png')
x, y = 0, 0
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
    for m in pubsub.listen():
        x = int(cx.get('x'))
        y = int(cx.get('y'))
        a = int(cx.get('a'))
        b = int(cx.get('b'))
        c = int(cx.get('c'))
        d = int(cx.get('d'))
        e = int(cx.get('e'))
        f = int(cx.get('f'))
        
        screen.blit(background, (0,0))
        screen.blit(angryBird, (x,y))
        screen.blit(angryGreenBird, (e,f))
        screen.blit(angryPiggy, (a,b))
        screen.blit(angryBlackBird, (c,d))
        pygame.display.update()
        

