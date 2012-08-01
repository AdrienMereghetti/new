# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *

dossier_name = 'rendu'
image_fs = 'Final_1'

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((600, 400)) 
pygame.display.set_caption('Visu photo')
screen = pygame.display.get_surface()
i = 1
exit_loop = 'no'
#Choix du défilement auto ou manuel des photos
while exit_loop != 'yes': 
    choix = pygame.image.load('image/choix.png')
    screen.blit(choix, (0,0))
    pygame.display.update()
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == pygame.locals.K_m:
                    choix = 'm'
                    exit_loop = 'yes'
                elif evt.key == pygame.locals.K_a:
                    choix = 'a' 
                    exit_loop = 'yes'
                else:
                    choix = 'e'      
                    exit_loop = 'yes'  
            else:
                pass

chargement = pygame.image.load('image/chargement.png')
screen.blit(chargement, (0,0))
pygame.display.update()
time.sleep(2)
'''#Réduit la résolution et la qualité de toutes les photos du dossier shoot
cmd = 'cd shoot && mkdir %s; for i in *.jpg; do convert -verbose -quality 50 -resize 800x600 "$i" "%s/$i"; done && mv %s ..' % (dossier_name, dossier_name, dossier_name)
subprocess.check_output(cmd, shell=True)
#Stack les photos basse qualité pour un rendu rapide
cmd2 = 'enfuse -o %s.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/*.jpg && mv %s.jpg %s' % (image_fs, dossier_name, image_fs, dossier_name)
subprocess.check_output(cmd2, shell=True)'''
#Defilement manuel des photos
if choix == 'm':
    go = pygame.image.load('image/go.png')
    screen.blit(go, (0,0))
    pygame.display.update()
    while True: 
        evts = pygame.event.get()
        if len(evts) > 0:
            for evt in evts:
                if evt.type == pygame.locals.KEYDOWN:
                    if evt.key == pygame.locals.K_LEFT:
                        if i >1:
                            i -= 1
                            image_name = 'Test_4-%i.jpg' % i
                        else:
                            image_name = 'Test_4.jpg'
                            
                    elif evt.key == pygame.locals.K_RIGHT:
                        if i <17:
                            i += 1
                            image_name = 'Test_4-%i.jpg' % i
                        else:
                            i = 18
                            image_name = '%s.jpg' % image_fs 
                    else:
                        image_name = 'Test_4-%i.jpg' % i
                    image = pygame.image.load('%s/%s' % (dossier_name, image_name))
                    screen.blit(image, (0,0))
                    pygame.display.update()
                    time.sleep(0.3)
        
                else:
                    pass                
#Défilement automatique des photos
elif choix == 'a':
    while True:
        image = pygame.image.load('%s/Test_4.jpg' % dossier_name)
        screen.blit(image, (0,0))
        pygame.display.update()
        time.sleep(0.3)
        for i in range(1,18):
            image_name = 'Test_4-%i.jpg' % i
            image = pygame.image.load('%s/%s' % (dossier_name, image_name))
            screen.blit(image, (0,0))
            pygame.display.update()
            time.sleep(0.3)

        final = pygame.image.load(('%s/%s.jpg') % (dossier_name, image_fs))
        screen.blit(final, (0,0))
        pygame.display.update()
        time.sleep(2)
#Message d'érreur        
elif choix == 'e':
    bad = pygame.image.load('image/bad.png')
    screen.blit(bad, (0,0))
    pygame.display.update()
    time.sleep(1)
    exit()
    
else:
    pass
