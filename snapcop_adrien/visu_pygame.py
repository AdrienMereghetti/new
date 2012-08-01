# -*- coding: utf-8 -*-

import redis
import pygame, sys, os, time
from pygame.locals import *

cx = redis.Redis()
pubsub = cx.pubsub()  
pubsub.subscribe(['sc:photo_taken'])

pygame.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Visu photo')
screen = pygame.display.get_surface()



while True:
    for m in pubsub.listen():
        chemin_image = m['data']
        image = pygame.image.load(chemin_image)
        screen.blit(image, (0,0))
        pygame.display.update()
        

