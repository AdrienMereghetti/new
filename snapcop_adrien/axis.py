# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

pygame.display.init()
pygame.joystick.init()
window = pygame.display.set_mode((3840, 1080)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()

a, b, c, d = 375, 275, 1175, 275

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
            '''if evt.type == pygame.locals.JOYBUTTONDOWN:
                i = evt.button
                if evt.button == i: # boutons
                    cx.publish('sc:joystick', str(i+1)) 
                else:
                    pass'''
            if evt.type == pygame.locals.JOYAXISMOTION:
                if evt.axis == 0:
                    a = int((evt.value + 1.0) * 375)
                    if a > 675:
                        a = 675
                    elif a < 75:
                        a = 75
                elif evt.axis == 1:
                    b = int((evt.value + 1.0) * 275)
                    c = 900 + (int((evt.value + 1.0) * 275))
                    if b > 475:
                        b = 475
                    elif b < 75:
                        b = 75
                    elif c > 1475:
                        c = 1475
                    elif c < 975:
                        c = 975
                elif evt.axis == 2:
                    d = int((evt.value + 1.0) * 275)
                    if d > 475:
                        d = 475
                    elif d < 75:
                        d = 75
                
                else: # cas non géré
                    pass
            
            else: # cas non géré
                pass
    background = pygame.image.load('image/background.png')
    x = pygame.image.load('image/x.gif')
    y = pygame.image.load('image/y.gif')
    y2 = pygame.image.load('image/y.gif')
    z = pygame.image.load('image/z.gif')
    screen.blit(background, (0,0))
    screen.blit(x, (a,275))
    screen.blit(y, (375, b))
    screen.blit(y2, (c,275))
    screen.blit(z, (1175, d))
    pygame.display.update()
