# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

import redis

pygame.joystick.init()
pygame.display.init()

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
                if evt.button == 0:
                    cx.publish('sc:take_photo', 'true')
                elif evt.button == 1:
                    cx.publish('sc:interface', 'launch')
                elif evt.button == 11:
                    cx.publish('sc:interface', 'quit')

            if evt.type == pygame.locals.JOYAXISMOTION:
                
                if evt.axis == 3:
                    if evt.value == 1:
                        cx.publish('sc:vitesse', '1')
                    elif evt.value < 0.9 and evt.value > 0:
                        cx.publish('sc:vitesse', '2')
                    elif evt.value == 0:
                        cx.publish('sc:vitesse', '3')
                    elif evt.value < 0 and evt.value > -0.9:
                        cx.publish('sc:vitesse', '4')
                    elif evt.value <= -1:
                        cx.publish('sc:vitesse', '5')
                    else:
                        pass
                
                elif evt.axis == 0:
                    if evt.value > 0.2:
                        cx.publish('sc:axis', 'x+')
                        axis_x = '+'
                    elif evt.value < -0.2:
                        cx.publish('sc:axis', 'x-')
                    else:
                        cx.publish('sc:axis', 'x0')
                        
                elif evt.axis == 1:
                    if evt.value > 0.2:
                        cx.publish('sc:axis', 'y+')
                    elif evt.value < -0.2:
                        cx.publish('sc:axis', 'y-')
                    else:
                        cx.publish('sc:axis', 'y0')

                elif evt.axis == 2:
                    if evt.value > 0.2:
                        cx.publish('sc:axis', 'z+')
                    elif evt.value < -0.2:
                        cx.publish('sc:axis', 'z-')
                    else:
                        cx.publish('sc:axis', 'z0')
                        
                
                    
                else: 
                   pass
                    
            else:
                pass
