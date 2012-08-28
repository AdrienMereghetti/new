#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import piggyphoto
import pygame
import pygame.locals
import redis
import shutil
import time
from wand.image import Image
from wand.display import display

cx = redis.Redis()
pubsub = cx.pubsub()  
pubsub.subscribe(['capture', 'stacking'])
pygame.display.init()
capture_on = False
stack_on = False

def preview():    
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == 27:
                    print "Fin du programme"
                    stop = True
    c = 0
    def afficherText(i, x, y, z, pos):
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        text = font.render(i, 1, (x, y, z))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        textpos.centery = background.get_rect().centery + pos
        screen.blit(text, textpos)
        pygame.font.quit()
    
    stop = False
    while not stop:
        for m in pubsub.listen():
            data = str(m['data'])
            if data[:6] == 'data/i':
                capture = m['data']    
                capture_on = True
                break
            if data[:6] == 'data/s':
                stack = m['data']    
                stack_on = True
                break
        if capture_on == True:
            c += 1
            nb_photo = int(cx.get('nb_photo'))
            window = pygame.display.set_mode((1920, 1080)) 
            pygame.display.set_caption('Capture Preview')
            screen = pygame.display.get_surface()
            evts = pygame.event.get()
           
                
            with Image(filename = capture) as img:
                with img.clone() as i:
                    i.resize((1920), (1080))
                    i.save(filename=capture)     
            preview = pygame.image.load(capture)
            screen.blit(preview, (0, 0))
            afficherText(("Photos prisent : %i/%i" % (c, nb_photo)), 255, 0, 255, 300)
            pygame.display.update()
            capture_on = False
        
        elif stack_on == True:
        
            window = pygame.display.set_mode((1920, 1080)) 
            pygame.display.set_caption('Capture Preview')
            screen = pygame.display.get_surface()
            evts = pygame.event.get()
               
            with Image(filename = stack) as img:
                with img.clone() as i:
                    i.resize((1920), (1080))
                    i.save(filename=stack)     
            preview = pygame.image.load(stack)
            screen.blit(preview, (0, 0))
            afficherText(("Photos Stack"), 255, 0, 255, 300)
            pygame.display.update()
            stack_on = False
            
