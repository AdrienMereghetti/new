#!/usr/bin/python

import time
import pygame
from pygame.locals import *

pygame.font.init()
pygame.display.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()

def afficherText(i):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    font = pygame.font.Font(None, 36)
    text = font.render(i, 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

afficherText('dcevse')
time.sleep(2)
