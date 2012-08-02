# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import *

pygame.joystick.init()

window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Axis Joystick 2')
screen = pygame.display.get_surface()
#positions image
a, b, c, d, e = 375, 275, 1175, 275, -300

axe_x, axe_y, axe_z = '0', '0', '0'

#Vérifie si un joystick est branché
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
            if evt.type == pygame.locals.JOYAXISMOTION:
                if evt.axis == 0:
                    if evt.value > 0.2:
                        axe_x = '+'
                    elif evt.value < -0.2:
                        axe_x = '-'
                    else:
                        axe_x = '0'

                elif evt.axis == 1:
                    if evt.value > 0.2 and evt.value < 0.9:
                        axe_y = '+'
                    elif evt.value > 0.9:
                        axe_y = '++'
                    elif evt.value < -0.2 and evt.value > -0.9:
                        axe_y = '-'
                    elif evt.value < -0.9:
                        axe_y = '--'
                    else:
                        axe_y = '0'
                
                elif evt.axis == 2:
                    if evt.value > 0.1 and evt.value < 0.9:
                        axe_z = '+'
                    elif evt.value > 0.9:
                        axe_z = '++'
                    elif evt.value < -0.1 and evt.value > -0.9:
                        axe_z = '-'
                    elif evt.value < -0.9:
                        axe_z = '--'
                    else:
                        axe_z = '0'
                        
    elif axe_x == '+':
        a += 1
        if a > 675:
            a = 675
    elif axe_x == '-':
        a -= 1
        if a < 75:
            a = 75
    elif axe_x == '++':
        a += 2
        if a > 675:
            a = 675
    elif axe_x == '--':
        a -= 2
        if a < 75:
            a = 75
    
    background = pygame.image.load('image/background.png')
    x = pygame.image.load('image/x.gif')
    screen.blit(background, (0,0))
    screen.blit(x, (a,275))
    pygame.display.update()
