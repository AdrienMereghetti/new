# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

import redis

pygame.init()
pygame.joystick.init()

cx = redis.Redis()

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()
    

while True: 
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == pygame.locals.K_ESCAPE:
                    exit = 1
            elif evt.type == pygame.locals.JOYAXISMOTION:
                print 'joy axis motion', evt.axis, evt.value
                if evt.axis == 0:
                    cx.set('joyx', evt.value)
                    cx.publish('c1', evt.value)
                elif evt.axis == 1:
                    cx.set('joyy', evt.value)
                    cx.publish('c1', evt.value)
            
            else:
                pass
                        
