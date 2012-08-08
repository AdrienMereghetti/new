# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *


pygame.font.init()
pygame.joystick.init()
pygame.display.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()

while True: 
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                shoot_nb = evt.unicode
                print shoot_nb + 10
                
                
                
