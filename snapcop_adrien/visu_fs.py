# -*- coding: utf-8 -*-

import redis
import pygame, sys, os, time
from pygame.locals import *

cx = redis.Redis()


a, b, c, d, e, f, g, h = 375, 275, 375, 275, 1175, 275, 1175, 275
vitesse, axe_x, axe_y, axe_z = 1, '0', '0', '0'

pubsub = cx.pubsub()  
pubsub.subscribe(['sc:vitesse', 'sc:axe_x', 'sc:axe_y', 'sc:axe_z', 'sc:interface'])

pygame.display.init()
window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()

while True:
    for m in pubsub.listen():
        if  m['channel'] == 'sc:interface':
            if m['data'] == 'quit':
                print 'fin  programme'
                exit()
        elif m['channel'] == 'sc:vitesse':
            vitesse = int(m['data'])
            print 'Vitesse = %i' % vitesse
            break
        elif m['channel'] == 'sc:axe_x':
            axe_x = m['data']
            print 'Axe_x = %s' % axe_x
            break
        elif m['channel'] == 'sc:axe_y':
            axe_y = m['data']
            print 'Axe_y = %s' % axe_y
            break
        elif m['channel'] == 'sc:axe_z':
            axe_z = m['data']
            print 'Axe_z = %s' % axe_z
            break
    
    if axe_x == '+':
        a += 1 * vitesse
        if a > 675:
            a = 675
        
    elif axe_x == '-':
        a -= 1 * vitesse
        
    elif axe_y == '+':
        b += 1 * vitesse
        c += 1.5 * vitesse
        
    elif axe_y == '-':
        b -= 1 * vitesse
        c -= 1.5 * vitesse
        
    elif axe_z == '+':
        d += 1 * vitesse
        
    elif axe_z == '-':
        d -= 1 * vitesse
        
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
        screen.blit(barre, (796, (-120*vitesse)))
        pygame.display.update()
