# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import *

pygame.joystick.init()

window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Axis Joystick 2')
screen = pygame.display.get_surface()

a, b, c, d, e = 375, 275, 1175, 275, -300

axe_x, axe_y, axe_z,  = '0', '0', '0'

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
                    if evt.value > 0.2 and evt.value < 0.9:
                        axe_x = '+'
                    elif evt.value > 0.9:
                        axe_x = '++'
                    elif evt.value < -0.2 and evt.value > -0.9:
                        axe_x = '-'
                    elif evt.value < -0.9:
                        axe_x = '--'
                    else:
                        axe_x = '0'

                if evt.axis == 1:
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
                
                if evt.axis == 2:
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
                        
                elif evt.axis == 3:
                    e =int((evt.value + 1.0) * -300)
                    if e < -600:
                        e = -600
                    elif e > 0:
                        e = 0
    
    
    if axe_x == '+':
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
            
    if axe_y == '+':
        b += 1
        if b > 475:
            b = 475
    elif axe_y == '-':
        b -= 1
        if b < 75:
            b = 75
    elif axe_y == '++':
        b += 2
        if b > 475:
            b = 475
    elif axe_y == '--':
        b -= 2
        if b < 75:
            b = 75
            
    if axe_y == '+':
        c += 1.5
        if c > 1475:
            c = 1475
    elif axe_y == '-':
        c -= 1.5
        if c < 875:
            c = 875
    elif axe_y == '++':
        c += 3
        if c > 1475:
            c = 1475
    elif axe_y == '--':
        c -= 3
        if c < 875:
            c = 875
            
    if axe_z == '+':
        d += 1
        if d > 475:
            d = 475
    elif axe_z == '-':
        d -= 1
        if d < 75:
            d = 75
    elif axe_z == '++':
        d += 2
        if d > 475:
            d = 475
    elif axe_z == '--':
        d -= 2
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
    screen.blit(barre, (796, e))
    pygame.display.update()
