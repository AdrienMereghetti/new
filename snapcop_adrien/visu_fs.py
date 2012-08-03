# -*- coding: utf-8 -*-

import redis
import pygame, sys, os, time
from pygame.locals import *

cx = redis.Redis()

a, b, c, d, e, f, g, h = 375, 275, 375, 275, 1175, 275, 1175, 275

pubsub = cx.pubsub()  
pubsub.subscribe(['sc:vitesse', 'sc:axis'])

'''pygame.display.init()
window = pygame.display.set_mode((1600, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()'''

while True:
    for m in pubsub.listen():
        if m['data'] == '1' or m['data'] == '2' or m['data'] == '3' or m['data'] == '4' or m['data'] == '5':
            vitesse = m['data']
        else:
            axis = m['data']
