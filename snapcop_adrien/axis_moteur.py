# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

pygame.display.init()
pygame.joystick.init()
pygame.font.init()
window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Axis Joystick')
screen = pygame.display.get_surface()

a, b, c, d, e = 375, 275, 1175, 275, -300

def afficherText(i):
    font = pygame.font.Font(None, 36)
    text = font.render(i, 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    screen.blit(text, textpos)
    pygame.display.flip()

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()


while True: 
        evts = pygame.event.get()
    #if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                i = evt.button
                if evt.button == i:
                    t = afficherText('Bouton %i' % (i + 1))
                    print t
                    time.sleep(1)
                '''elif evt.button == 11:
                    afficherText('Fin du programme')
                    time.sleep(2)
                    exit()
                else:
                    pass'''
                    
            if evt.type == pygame.locals.JOYAXISMOTION:
                if evt.axis == 0:
                    if evt.value > 0.2: 
                        a += 1
                        if a > 675:
                            a = 675
                    elif evt.value < - 0.2:
                        a -= 1
                        if a < 75:
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
                    d = 75 +(int((evt.value + 1.0) * 200))
                    if d > 475:
                        d = 475
                    elif d < 75:
                        d = 75
                
                elif evt.axis == 3:
                    e =int((evt.value + 1.0) * -300)
                    if e < -600:
                        e = -600
                    elif e > 0:
                        e = 0
                
                else: 
                    pass
            
            else:
                pass
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
