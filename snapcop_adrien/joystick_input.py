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
                #Partie prise de vue
                if evt.button == 0:
                    cx.publish('sc:take_photo', 'true')
                #Interface graphique
                elif evt.button == 1:
                    cx.publish('sc:interface', 'launch')
                    
                elif evt.button == 11:
                    cx.publish('sc:interface', 'quit')

            if evt.type == pygame.locals.JOYAXISMOTION:
                # Partie moteur
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
                        cx.publish('sc:axe_x', '+')
                        axis_x = '+'
                    elif evt.value < -0.2:
                        cx.publish('sc:axe_x', '-')
                    else:
                        cx.publish('sc:axe_x', '0')
                        
                elif evt.axis == 1:
                    if evt.value > 0.2:
                        cx.publish('sc:axe_y', '+')
                    elif evt.value < -0.2:
                        cx.publish('sc:axe_y', '-')
                    else:
                        cx.publish('sc:axe_y', '0')

                elif evt.axis == 2:
                    if evt.value > 0.2:
                        cx.publish('sc:axe_z', '+')
                    elif evt.value < -0.2:
                        cx.publish('sc:axe_z', '-')
                    else:
                        cx.publish('sc:axe_z', '0')
                        
                
                    
                else: 
                    cx.publish('sc:axe_z', '0')
                    			
            else:
                pass
    else:
        pass
