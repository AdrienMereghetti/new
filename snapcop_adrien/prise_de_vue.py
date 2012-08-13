#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time, subprocess
import pygame
from pygame.locals import *

day = time.strftime("%d-%m-%Y", time.localtime())
dossier = 'shoot-%s' % day
dossier_name = 'rendu-%s' % day
i = 1
shoot_nb = 1
image_fs = 'Final_%i' % shoot_nb
interval = 10
frames = 1
photos_name = 'O26_'

souche = 'Capuchon clé USB'
mycelium = 0
spore = 0

pygame.font.init()
pygame.joystick.init()
pygame.display.init()
window = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('Visu photo stacker %s' % day)
screen = pygame.display.get_surface()

exit_loop1 = 'no'
exit_loop2 = 'no'
exit_loop3 = 'no'
cmd3 = 'rm -rf %s' % dossier_name

try:
    os.mkdir(dossier)
except:
    pass
    
try:
    os.mkdir('%s/%s' % (dossier, dossier_name))
except:
    pass

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
    
def indicateur():
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 30)
    text = font.render(('Codification souche : %s' % souche), 1, (255, 0, 255))
    text2 = font.render(('Nombre de spore : %s' % spore), 1, (255, 0, 255))
    text3 = font.render(('Surface du mycelium %s' % mycelium), 1, (255, 0, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + 325
    text2pos = text.get_rect()
    text2pos.centerx = background.get_rect().centerx
    text2pos.centery = background.get_rect().centery + 350
    text3pos = text.get_rect()
    text3pos.centerx = background.get_rect().centerx
    text3pos.centery = background.get_rect().centery + 375
    screen.blit(background, (0, 0))
    screen.blit(text, textpos)
    screen.blit(text2, text2pos)
    screen.blit(text3, text3pos)

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
                if evt.key == 27:
                    exit = afficherText("Fin du programme", 255, 0, 255)
                    print exit
                    time.sleep(2)
                    exit()
                else:
                    shoot_nb = int(evt.unicode)
                    exit_loop1 = 'yes'
                
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

#Choix nombre de photos a prendre
while exit_loop3 != 'yes': 
    choix3 = afficherText2l("Combien de photos souhaitez -vous prendre?", "Bouton joystick :5=5 6=10 7=15 8=20 9=25 10=30", 255, 0, 255) 
    print choix3
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                i = evt.button
                frames = ((i-3)*5)
                      
                if frames == -15:
                    frames = 1
                    nb_frames = afficherText(("Vous avez choisi de prendre 1 photos"), 255, 0, 255) 
                    print nb_frames
                    time.sleep(2)
                    exit_loop3 = 'yes'        
                if frames >=5 and frames <=30:
                    nb_frames = afficherText(("Vous avez choisi de prendre %i photos" % frames), 255, 0, 255) 
                    print nb_frames
                    time.sleep(2)
                    exit_loop3 = 'yes'
                if evt.button == 11:
                    exit = afficherText("Fin du programme", 255, 0, 255)
                    print exit
                    time.sleep(2)
                    exit()
                else:
                    pass
                
            else:
                pass
#Prise de vue
for a in range(0, 4):
    j = '.' * a
    shooting = afficherText(("Prise de vue en cour %s" % j), 255, 0, 255) 
    print shooting
    time.sleep(0.5)
    
for i in range(0, frames):
    filename = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
    cmd = 'sudo gphoto2 --capture-image-and-download --force-overwrite --filename %s && sudo mv %s %s' % (filename, filename, dossier)
    shooting = afficherText(("Photos prisent : %i/%i" % (i+1, frames)), 255, 0, 255) 
    print shooting
    subprocess.check_output(cmd, shell=True)
    

for a in range(0, 4):
    j = '.' * a
    chargement = afficherText(("Chargement %s" % j), 255, 0, 255) 
    print chargement
    time.sleep(0.5)    

#Réduit la résolution et la qualité de toutes les photos du dossier shoot
cmd = 'cd %s; for i in %s%i*.jpg; do convert -quality 50 -resize 800x600 "$i" "%s/$i"; done && cp -R %s .. && rm -rf %s' % (dossier, photos_name, shoot_nb, dossier_name, dossier_name, dossier_name)
subprocess.check_output(cmd, shell=True)
'''try:
    shutil.move('%s ..' % dossier_name)
except:
    pass'''
#Stack les photos basse qualité pour un rendu rapide
cmd2 = 'enfuse -o %s.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/*.jpg && mv %s.jpg %s' % (image_fs, dossier_name, image_fs, dossier_name)
subprocess.check_output(cmd2, shell=True)
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
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            image_name = '%s%i.jpg' % (photos_name, shoot_nb)
                            
                    elif evt.value[0] == 1 and evt.value[1] == 0:
                        if i <(frames-1):
                            i += 1
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            i = (frames-1)
                            image_name = '%s%i.jpg' % (photos_name, image_fs, shoot_nb)
                        
                        
                    elif evt.value[0] == 0 and evt.value[1] == 1:
                        if shoot_nb >3:
                            shoot_nb -= 1
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            image_name = '%s%i.jpg' % (photos_name, shoot_nb)
                            
                    elif evt.value[0] == 0 and evt.value[1] == -1:
                        if shoot_nb <4:
                            shoot_nb += 1
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            shoot_nb = 4
                            image_name = '%s%i.jpg' % (photos_name, image_fs, shoot_nb)
                        
                    else:
                        image_name = '%s%i-%i.jpg' % (shoot_nb, i)
                    image = pygame.image.load('%s/%s' % (dossier_name, image_name))
                    screen.blit(image, (0,0))
                    pygame.display.update()
                    time.sleep(0.3)
                
                if evt.type == pygame.locals.JOYBUTTONDOWN:
                    if evt.button == 1:
                        image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        image = pygame.image.load('%s/%s' % (dossier_name, image_name))
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
        for i in range(0,(frames)):
            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
            image = pygame.image.load('%s/%s' % (dossier_name, image_name))
            screen.blit(image, (0,0))
            pygame.display.update()
            time.sleep(0.5)
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
        final = pygame.image.load(('%s/%s.jpg') % (dossier_name, image_fs))
        indicateur()
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
