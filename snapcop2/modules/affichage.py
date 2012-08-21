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
pubsub.subscribe(['capture'])


def preview():    
    stop = False
    while not stop:
        for m in pubsub.listen():
                capture = m['data']
                capture_on = True
                break
        if capture_on == True:
            pygame.display.init()
            window = pygame.display.set_mode((800, 600)) 
            pygame.display.set_caption('Capture Preview')
            screen = pygame.display.get_surface()
            evts = pygame.event.get()
            if len(evts) > 0:
                for evt in evts:
                    if evt.type == pygame.locals.KEYDOWN:
                        if evt.key == 27:
                            print "Fin du programme"
                            stop = True
                
                with Image(filename = capture) as img:
                    with img.clone() as i:
                        i.resize((800), (600))
                        i.save(filename=capture)
                        time.sleep(0.3)       
                preview = pygame.image.load(capture)
                screen.blit(preview, (0, 0))
                pygame.display.update()
                time.sleep(3)
            capture_on = False
            pygame.display.quit()
            
