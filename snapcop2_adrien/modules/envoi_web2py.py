#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import pygame
import pygame.locals
import redis
import shutil
import sys
import time
from wand.image import Image

pygame.display.init()
window = pygame.display.set_mode((1, 1)) 
pygame.display.set_caption('web2py')
screen = pygame.display.get_surface()



def main():
    cx = redis.Redis()
    ps = cx.pubsub()
    ps.subscribe(['envoi', 'exit'])
    for m in ps.listen():
        data = str(m['data'])
        if data[:3] == 'sys':
                sys.exit()
        print 'Envoi!'
        frames = int(cx.get('frames'))
        # On récupère les x dernières photos
        serie = cx.lrange('captures', -frames, -1)
        for i in range(0, frames):
            dest = '../web2py/applications/snapcop2_web2py/static/Photos'
            shutil.copy2(serie[i], dest)
            image = serie[i]
            image='%s/%s'%(dest, image[-22:])
            with Image(filename = image) as img:
                with img.clone() as i:
                    i.resize((100), (67))
                    i.save(filename='%sthumb%s'% (image[:-22], image[-18:]))
