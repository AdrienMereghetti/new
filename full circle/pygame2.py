#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *

couleurFond = 0, 255, 127
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
ecran = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Fantome')
ecran.fill(couleurFond)

class Fantome(pygame.sprite.Sprite):
    def __init__(self, position):
        
        pygame.sprite.Sprite.__init__(self)
        self.ecran = pygame.display.get_surface().get_rect()
        self.ancienFantome = (0, 0, 0, 0)
        self.image = pygame.image.load('cross.png')
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def metAJour(self, valeur):
        self.ancienFantome = self.rect
        self.rect = self.rect.move(valeur)
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > (self.ecran.width - self.rect.width):
            self.rect.x = self.ecran.width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > (self.ecran.height - self.rect.height):
            self.rect.y = self.ecran.height - self.rect.height
            
personnage = Fantome((ecran.get_rect().x, ecran.get_rect().y))
ecran.blit(personnage.image, personnage.rect)
rectangleBlanc = pygame.Surface((personnage.rect.width, personnage.rect.height))
rectangleBlanc.fill(couleurFond)

pygame.display.update()
faireBoucle = 1
while faireBoucle:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            sys.exit()
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_LEFT:
                personnage.metAJour([-10, 0])
            elif evt.key == pygame.K_UP:
                personnage.metAJour([0, -10])
            elif evt.key == pygame.K_RIGHT:
                personnage.metAJour([10, 0])
            elif evt.key == pygame.K_DOWN:
                personnage.metAJour([0, 10])
            elif evt.key == pygame.K_q:
                faireBoucle = 0
    ecran.blit(rectangleBlanc, personnage.ancienFantome)
    ecran.blit(personnage.image, personnage.rect)
    pygame.display.update([personnage.ancienFantome, personnage.rect])
    

