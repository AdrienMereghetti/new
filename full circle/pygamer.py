#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *
 
couleurFond = 208, 202, 104
couleurPolice = 255,255,255


os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
ecran = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Test #1')
ecran.fill(couleurFond)
arial = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
police = pygame.font.Font(arial,27)
police.set_italic(True)
texte = police.render('Texte test texte', True, couleurPolice, couleurFond)
texte_rect = texte.get_rect()
texte_rect.centerx = ecran.get_rect().centerx
texte_rect.centery = ecran.get_rect().centery
ecran.blit(texte, texte_rect)  
pygame.display.update()


faireBoucle = 1

while faireBoucle:
    if pygame.event.wait().type in (KEYDOWN, MOUSEBUTTONDOWN): 
        break
