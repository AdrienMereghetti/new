#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import piggyphoto
import pygame
import pygame.locals
import redis
import shutil
import time
from wand.image import Image
from wand.display import display


#pygame.font.init()
pygame.joystick.init()
pygame.display.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Display Preview')
screen = pygame.display.get_surface()

def main():
    print 'capture ...'

    camera = piggyphoto.camera()
    camera.leave_locked()

    cx = redis.Redis()
    
    stop = False
    while not stop:    
        time.sleep(0.)
        print time.time(), 'capture preview ...'
        camera.capture_preview('data/preview.jpg')
        with Image(filename='data/preview.jpg') as img:
            with img.clone() as i:
                i.resize((800), (600))
                i.save(filename='data/preview.jpg')      
        preview = pygame.image.load('data/preview.jpg')
        screen.blit(preview, (0, 0))
        pygame.display.update()
        
        cx.publish('preview', '')
        
        
        evts = pygame.event.get()
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == 27:
                    print "Fin du programme"
                    stop = True
                elif evt.key == 112: # P
                    pass
                elif evt.key == 99: # C
                    print 'capture image ...'
                    source_capture = 'data/capture.jpg'
                    camera.capture_image(source_capture)
                    
                    # obtenir les infos saisis
                    auteur = cx.get('auteur')
                    souche = cx.get('souche')
                    desc = cx.get('desc')
                    
                    # Modifier les données "EXIF"
                    print "info:", auteur, desc
                    
                    # Déplacer la photo 
                    time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
                    dest_capture = os.path.join('data/images', 'capt%s.jpg' % time_stamp)
                    shutil.move(source_capture, dest_capture)
                    
                    # On ajoute à la liste des photos prises
                    cx.rpush('captures', dest_capture)
                    # trim de la liste ???
                    
                    # on informe qu'une capture vient d'être faite
                    cx.publish('capture', dest_capture)

                elif evt.key == 115: # S
                    print 'demande de stacking rapide ...'
                    cx.publish('stack_rapide', '')

                elif evt.key == 116: # T
                    print 'demande de stacking lent ...'
                    cx.publish('stack_lent', '')
                    
                else:
                    print 'touche inconnue ', evt.key

