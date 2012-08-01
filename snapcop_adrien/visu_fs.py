# -*- coding: utf-8 -*-

import redis
import pygame, sys, os, time
from pygame.locals import *

cx = redis.Redis()

a, b, c, d, e, f, g, h = 375, 275, 375, 275, 1175, 275, 1175, 275

pubsub = cx.pubsub()  
pubsub2 = cx.pubsub()
pubsub.subscribe(['sc:joystick'])

pygame.display.init()
window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()

while True:
    for m in pubsub.listen():
        if int(m['data']) <=12:
            print 'Button %s' % m['data']
        elif int(m['data']) > 12:
            print 'Axis Motion'
        a = cx.get('a')
        background = pygame.image.load('image/background.png')
        x = pygame.image.load('image/x.gif')
        y = pygame.image.load('image/y.gif')
        y2 = pygame.image.load('image/y.gif')
        z = pygame.image.load('image/z.gif')
        screen.blit(background, (0,0))
        screen.blit(x, (a,b))
        screen.blit(y, (c,d))
        screen.blit(y2, (e,f))
        screen.blit(z, (g,h))
        pygame.display.update()
