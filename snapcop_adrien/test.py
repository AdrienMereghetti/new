# -*- coding: utf-8 -*-

import usb,redis,  pygame, sys, os, time, subprocess
import pygame.locals

pygame.display.init()
window = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()

shoot_nb = ''
loop = False

cx = redis.Redis()
cx.publish('shoot', '-1')
'''while not loop:
            
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == 27:
                    exit = afficherText("Fin du programme", 255, 0, 255, 0)
                    print exit
                    time.sleep(2)
                    exit()
                    
                elif evt.key == 13:
                    loop = True
                else:
                    shoot_nb += '%s' % evt.unicode
                    print shoot_nb'''
