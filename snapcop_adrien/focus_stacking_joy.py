# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *

dossier_name = 'rendu'
image_fs = 'Final_'

pygame.font.init()
pygame.joystick.init()
pygame.display.init()
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Visu photo stacker')
screen = pygame.display.get_surface()
shoot_nb = 4
i = 1
exit_loop1 = 'no'
exit_loop2 = 'no'
cmd3 = 'rm -rf %s' % dossier_name

def afficherText(i, x, y, z):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render(i, 1, (x, y, z))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    screen.blit(background, (0, 0))
    screen.blit(text, textpos)
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

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()

#Choix du numéro de shoot
while exit_loop1 != 'yes': 
    choix1 = afficherText("Indiquez le numero du shoot a l'aide du clavier numerique", 255, 0, 255)
    print choix1
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
                elif evt.key == 27:
                    exit = afficherText("Fin du programme", 255, 0, 255)
                    print exit
                    time.sleep(2)
                    exit()
                elif evt.key != 259 or evt.key != 260 or evt.key != 27:
                    bad = afficherText("Votre choix n'est pas correct ! Relancez le script", 255, 0, 255)
                    print bad
                    time.sleep(2)
                    exit()
                else:
                    choix = 'e'      
                    exit_loop1 = 'yes'  
            else:
                pass
                
#Choix du défilement auto ou manuel des photos
while exit_loop2 != 'yes': 
    choix2 = afficherText2l("Voulez-vous un defilement automatique(a)", "ou manuel(m) des photos ?", 255, 0, 255) 
    print choix2
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
                    exit = afficherText("Fin du programme", 255, 0, 255)
                    print exit
                    time.sleep(2)
                    exit()
                else:
                    choix = 'e'      
                    exit_loop2 = 'yes'  
            else:
                pass

for a in range(0, 4):
    j = '.' * a
    chargement = afficherText(("Chargement %s" % j), 255, 0, 255) 
    print chargement
    time.sleep(0.5)
'''#Réduit la résolution et la qualité de toutes les photos du dossier shoot
cmd = 'cd shoot && mkdir %s; for i in Test_%i*.jpg; do convert -quality 50 -resize 800x600 "$i" "%s/$i"; done && mv %s ..' % (dossier_name, shoot_nb, dossier_name, dossier_name)
subprocess.check_output(cmd, shell=True)
#Stack les photos basse qualité pour un rendu rapide
cmd2 = 'enfuse -o %s%i.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/*.jpg && mv %s%i.jpg %s' % (image_fs, shoot_nb, dossier_name, image_fs, shoot_nb, dossier_name)
subprocess.check_output(cmd2, shell=True)'''
#Defilement manuel des photos
if choix == 'm':
    go = afficherText("Utilisez le HAT du Joystick pour faire defiler les photos", 255, 0, 255)
    print go
        
    while True: 
        evts = pygame.event.get()
        if len(evts) > 0:
            for evt in evts:
                if evt.type == pygame.locals.JOYHATMOTION:
                    if evt.value[0] == -1 and evt.value[1] == 0:
                        if i >1:
                            i -= 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            image_name = 'Test_%i.jpg' % shoot_nb
                            
                    elif evt.value[0] == 1 and evt.value[1] == 0:
                        if i <17:
                            i += 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            i = 17
                            image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        
                        
                    elif evt.value[0] == 0 and evt.value[1] == 1:
                        if shoot_nb >3:
                            shoot_nb -= 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            image_name = 'Test_%i.jpg' % shoot_nb
                            
                    elif evt.value[0] == 0 and evt.value[1] == -1:
                        if shoot_nb <4:
                            shoot_nb += 1
                            image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                        else:
                            shoot_nb = 4
                            image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        
                    else:
                        image_name = 'Test_%i-%i.jpg' % (shoot_nb, i)
                    image = pygame.image.load('%s/%s' % (dossier_name, image_name))
                    screen.blit(image, (0,0))
                    pygame.display.update()
                    time.sleep(0.3)
                
                if evt.type == pygame.locals.JOYBUTTONDOWN:
                    if evt.button == 1:
                        image = pygame.image.load('%s/%s' % (dossier_name, image_name))
                        image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        screen.blit(image, (0,0))
                        pygame.display.update()
                
                if evt.type == pygame.locals.JOYBUTTONDOWN:
                    if evt.button == 11:
                        exit = afficherText("Fin du programme", 255, 0, 255)
                        print exit
                        time.sleep(2)
                        exit()
                        
                    
                
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
            evts = pygame.event.get()
            if len(evts) > 0:
                for evt in evts:
                    if evt.type == pygame.locals.KEYDOWN:
                        if evt.key == 27:
                            exit = afficherText("Fin du programme", 255, 0, 255)
                            print exit
                            time.sleep(2)
                            #subprocess.check_output(cmd3, shell=True)
                            exit()
                        else: 
                            pass
        final = pygame.image.load(('%s/%s%i.jpg') % (dossier_name, image_fs, shoot_nb))
        screen.blit(final, (0,0))
        pygame.display.update()
        time.sleep(2)
        
#Message d'érreur        
elif choix == 'e':
    bad = afficherText("Votre choix n'est pas correct ! Relancez le script", 255, 0, 255)
    print bad
    time.sleep(2)
    exit()
    
else:
    pass
