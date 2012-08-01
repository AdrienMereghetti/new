# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

import redis

pygame.display.init()
pygame.joystick.init()

cx = redis.Redis()
cx2 = redis.Redis()

a, b, c, d, e, f, g, h = 375, 275, 375, 275, 1175, 275, 1175, 275

cx.set('a', a)
#cx.set('f', f)
cx.publish('sc:joystick', a)
#cx.publish('sc:joystick', b)


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
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                i = evt.button
                if evt.button == i: # boutons
                    cx.publish('sc:joystick', str(i+1)) 
                else:
                    pass
            elif evt.type == pygame.locals.JOYAXISMOTION:
                if evt.axis == 0:
                    a = int((evt.value + 1.0) * 375)
                    if a > 775:
                        a = 775
                    elif a < 75:
                        a = 75
                    cx.set('a', a)
                    cx.publish('sc:joystick', a)
                elif evt.axis == 1:
                    b = 100
                    cx.publish('sc:joystick', b)
                elif evt.axis == 2:
                    c = 500
                    cx.publish('sc:joystick', c)
                elif evt.axis == 3:
                    d = 1000
                    cx.publish('sc:joystick', d)
                
                else: # cas non géré
                    pass
            else: # cas non géré
                pass
