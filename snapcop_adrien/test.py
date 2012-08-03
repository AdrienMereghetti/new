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

def afficherText(i,txt, x, y, z):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    screen.blit(background, (0, 0))
    for j in (0, (i+1)):
        text(j) = font.render(txt, 1, (x, y, z))
        textpos(j) = text.get_rect()
        textpos(j).centerx = background.get_rect().centerx
        textpos(j).centery = background.get_rect().centery + 25*j
        screen.blit(text(j), textpos(j))
    pygame.display.flip()
    
def afficherText2l(i, j, x, y, z):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render(i, 1, (x, y, z))
    text2 = font.render(j, 1, (x, y, z))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    text2pos = text.get_rect()
    text2pos.centerx = background.get_rect().centerx
    text2pos.centery = background.get_rect().centery + 25
    screen.blit(background, (0, 0))
    screen.blit(text, textpos)
    screen.blit(text2, text2pos)
    pygame.display.flip()
    

