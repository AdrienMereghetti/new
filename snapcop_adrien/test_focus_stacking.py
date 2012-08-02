# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *

dossier_name = 'rendu'
image_fs = 'Final_'

pygame.display.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()
shoot_nb = 4
i = 1
exit_loop1 = 'no'
exit_loop2 = 'no'
cmd3 = 'rm -rf %s' % dossier_name
#Choix du numéro de shoot
while exit_loop1 != 'yes': 
    choix = pygame.image.load('image/choix1.png')
    screen.blit(choix, (0,0))
    pygame.display.update()
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == 259:
                    shoot_nb = 3
                    exit_loop1 = 'yes'
                elif evt.key == 260:
                    shoot_nb = 4 
                    exit_loop1 = 'yes'
                elif evt.key != 259 or evt.key != 260 or evt.key != 27:
                    bad = pygame.image.load('image/bad.png')
                    screen.blit(bad, (0,0))
                    pygame.display.update()
                    time.sleep(1)
                    exit()
                elif evt.key == 27:
                    exit = pygame.image.load('image/exit.png')
                    screen.blit(exit, (0,0))
                    pygame.display.update()
                    time.sleep(2)
                    exit()
                else:
                    choix = 'e'      
                    exit_loop1 = 'yes'  
            else:
                pass
#Choix du défilement auto ou manuel des photos
while exit_loop2 != 'yes': 
    choix = pygame.image.load('image/choix2.png')
    screen.blit(choix, (0,0))
    pygame.display.update()
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.KEYDOWN:
                if evt.key == pygame.locals.K_m:
                    choix = 'm'
                    exit_loop2 = 'yes'
                elif evt.key == pygame.locals.K_a:
                    choix = 'a' 
                    exit_loop2 = 'yes'
                elif evt.key == 27:
                    exit = pygame.image.load('image/exit.png')
                    screen.blit(exit, (0,0))
                    pygame.display.update()
                    time.sleep(1)
                    exit()
                else:
                    choix = 'e'      
                    exit_loop2 = 'yes'  
            else:
                pass


chargement = pygame.image.load('image/chargement.png')
screen.blit(chargement, (0,0))
pygame.display.update()
time.sleep(1)
'''#Réduit la résolution et la qualité de toutes les photos du dossier shoot
cmd = 'cd shoot && mkdir %s; for i in Test_%i*.jpg; do convert -quality 50 -resize 800x600 "$i" "%s/$i"; done && mv %s ..' % (dossier_name, shoot_nb, dossier_name, dossier_name)
subprocess.check_output(cmd, shell=True)
#Stack les photos basse qualité pour un rendu rapide
cmd2 = 'enfuse -o %s%i.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/*.jpg && mv %s%i.jpg %s' % (image_fs, shoot_nb, dossier_name, image_fs, shoot_nb, dossier_name)
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
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            image_name = 'Test_%i.jpg' % shoot_nb
                            
                    elif evt.key == pygame.locals.K_RIGHT:
                        if i <17:
                            i += 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            i = 17
                            image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                            
                    elif evt.key == pygame.locals.K_SPACE:
                        image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        
                        
                        
                    elif evt.key == pygame.locals.K_DOWN:
                        if shoot_nb >3:
                            shoot_nb -= 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            image_name = 'Test_%i.jpg' % shoot_nb
                            
                    elif evt.key == pygame.locals.K_UP:
                        if shoot_nb <4:
                            shoot_nb += 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            shoot_nb = 4
                            image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        
                        
                        
                        
                    elif evt.key == 27:
                        exit = pygame.image.load('image/exit.png')
                        screen.blit(exit, (0,0))
                        pygame.display.update()
                        time.sleep(1)
                        #subprocess.check_output(cmd3, shell=True)
                        exit()
                    else:
                        image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                    image = pygame.image.load('%s/%s' % (dossier_name, image_name))
                    screen.blit(image, (0,0))
                    pygame.display.update()
                    time.sleep(0.3)
        
                else:
                    pass                
#Défilement automatique des photos
elif choix == 'a':
    while True:
        image = pygame.image.load('%s/Test_%i.jpg' % (dossier_name, shoot_nb))
        screen.blit(image, (0,0))
        pygame.display.update()
        time.sleep(0.3)
        for i in range(1,18):
            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
            image = pygame.image.load('%s/%s' % (dossier_name, image_name))
            screen.blit(image, (0,0))
            pygame.display.update()
            time.sleep(0.3)

        final = pygame.image.load(('%s/%s%i.jpg') % (dossier_name, image_fs, shoot_nb))
        screen.blit(final, (0,0))
        pygame.display.update()
        time.sleep(2)
        evts = pygame.event.get()
        if len(evts) > 0:
            for evt in evts:
                if evt.type == pygame.locals.KEYDOWN:
                    if evt.key == 27:
                        exit = pygame.image.load('image/exit.png')
                        screen.blit(exit, (0,0))
                        pygame.display.update()
                        time.sleep(1)
                        #subprocess.check_output(cmd3, shell=True)
                        exit()
                    else: 
                        pass
#Message d'érreur        
elif choix == 'e':
    bad = pygame.image.load('image/bad.png')
    screen.blit(bad, (0,0))
    pygame.display.update()
    time.sleep(2)
    exit()
    
else:
    pass
