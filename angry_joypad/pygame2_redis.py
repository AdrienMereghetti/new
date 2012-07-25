# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

import redis

pygame.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Angry')
screen = pygame.display.get_surface()
pygame.display.update()
cx = redis.Redis()

x, y = 400, 200
while True: 
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            #Mouvement du red bird grâce fleche du clavier        
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == pygame.locals.K_LEFT:
                    x -= 10
                    if x < 0:
                        x = 0
                    cx.set('x', x)
                    cx.publish('c1', x)
                
                elif evt.key == pygame.locals.K_RIGHT:
                    x += 10
                    if x > 600:
                        x = 600
                    cx.set('x', x)
                    cx.publish('c1', x)
                    
                elif evt.key == pygame.locals.K_DOWN:
                    y += 10
                    if y > 400:
                        y = 400
                    cx.set('y', y)
                    cx.publish('c1', y)
                
                elif evt.key == pygame.locals.K_UP:
                    y -= 10
                    if y < 0:
                        y = 0
                    cx.set('y', y)
                    cx.publish('c1', y)
            
            else:
                pass
                        
