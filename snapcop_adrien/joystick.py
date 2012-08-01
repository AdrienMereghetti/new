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
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                if evt.button == 0: # bouton A
                    cx.publish('sc:take_photo', '1')
                elif evt.button == 1: # bouton B
                    cx.publish('sc:take_photo', '5')
                    
                else: # cas non géré
                    print evt
            else: # cas non géré
                print evt

