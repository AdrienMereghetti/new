#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
import pygame.locals

pygame.joystick.init()
pygame.display.init()
window = pygame.display.set_mode((1056, 704)) 
pygame.display.set_caption('Display Preview')
screen = pygame.display.get_surface()

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()


while True:
    evts = pygame.event.get()
    for evt in evts:
        if evt.type == pygame.locals.KEYDOWN:
            print evt.key
