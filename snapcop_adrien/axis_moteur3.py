# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import *

pygame.joystick.init()

window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Axis Joystick 3')
screen = pygame.display.get_surface()
#positions image
a, b, c, d = 375, 275, 1175, 275

vitesse, axe_x, axe_y, axe_z = 1, '0', '0', '0'

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
            
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                if evt.button == 11:
                    exit()
            
            elif evt.type == pygame.locals.JOYAXISMOTION:
            
                if evt.axis == 0:
                    if evt.value > 0.2:
                        axe_x = '+'
                    elif evt.value < -0.2:
                        axe_x = '-'
                    else:
                        axe_x = '0'
                        
                elif evt.axis == 1:
                    if evt.value > 0.2:
                        axe_y = '+'
                    elif evt.value < -0.2:
                        axe_y = '-'
                    else:
                        axe_y = '0'

                elif evt.axis == 2:
                    if evt.value > 0.1:
                        axe_z = '+'
                    elif evt.value < -0.1:
                        axe_z = '-'
                    else:
                        axe_z = '0'
                        
                elif evt.axis == 3:
                    if evt.value == 1:
                        vitesse = 1
                    elif evt.value < 0.9 and evt.value > 0:
                        vitesse = 2
                    elif evt.value == 0:
                        vitesse = 3
                    elif evt.value < 0 and evt.value > -0.9:
                        vitesse = 4
                    elif evt.value <= -1:
                        vitesse = 5
                    else:
                        pass
                        
                        
                        
                    
    if axe_x == '+':
        a += 1 * vitesse
        if a > 675:
            a = 675
    elif axe_x == '-':
        a -= 1 * vitesse
        if a < 75:
            a = 75

    elif axe_y == '+':
        b += 1 * vitesse
        c += 1.5 * vitesse
        if b > 475 and c > 1175:
            b, c = 475, 1175
        elif b > 475:
            b = 475
        elif c > 1175:
            c = 1175
    elif axe_y == '-':
        b -= 1 * vitesse
        c -= 1.5 * vitesse
        if b < 75 and c < 875:
            b, c = 75, 875
        elif b < 75:
            b = 75
        elif c < 875:
            c = 875

    elif axe_z == '+':
        d += 1 * vitesse
        if d > 475:
            d = 475
    elif axe_z == '-':
        d -= 1 * vitesse
        if d < 75:
            d = 75
        

        
    background = pygame.image.load('image/background.png')
    x = pygame.image.load('image/x.gif')
    y = pygame.image.load('image/y.gif')
    y2 = pygame.image.load('image/y.gif')
    z = pygame.image.load('image/z.gif')
    barre = pygame.image.load('image/barre.png')
    screen.blit(background, (0,0))
    screen.blit(x, (a,275))
    screen.blit(y, (375, b))
    screen.blit(y2, (c,275))
    screen.blit(z, (1175, d))
    screen.blit(barre, (796, (-120*vitesse)))
    pygame.display.update()
