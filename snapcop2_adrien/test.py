#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *

while True:
    window = pygame.display.set_mode((800, 600)) 
    pygame.display.set_caption('Capture Preview')
    screen = pygame.display.get_surface()
    pygame.display.update()

    evts = pygame.event.get()
    for evt in evts:
        if evt.type == pygame.locals.KEYDOWN:
            print evt
