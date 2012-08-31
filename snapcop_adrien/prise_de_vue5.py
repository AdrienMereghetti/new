#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import piggyphoto
import pygame
import pygame.locals
import redis
import shutil
import time
import subprocess
import sys
from wand.image import Image

import time, redis
day = time.strftime("%d-%m-%Y", time.localtime())
cx = redis.Redis()

dossier = '%s-%s' % ((str(cx.get('dossier'))), day)
dossier_name = '%s-%s' % ((str(cx.get('dossier_name'))), day)
image_fs = '%s_'%(str(cx.get('image_fs')))
interval = int(cx.get('interval'))
photos_name = '%s_'%str(cx.get('photos_name'))
souche = str(cx.get('souche'))
defil = str(cx.get('defil'))

os.environ['SDL_VIDEO_CENTERED'] = '1'

i = 0
shoot_nb = -1
frames = 1
mycelium = '~0'
spore = '~0'

pygame.font.init()
pygame.joystick.init()
pygame.display.init()
window = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('Visu photo stacker %s' % day)
screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
background = background.convert()

exit_loop1 = 'no'

camera = piggyphoto.camera()
camera.leave_locked()

try:
    os.mkdir(dossier)
except:
    pass
    
try:
    os.mkdir(dossier_name)
except:
    pass

#Affichage d'un texte centré
def afficherText(i, x, y, z, pos):
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render(i, 1, (x, y, z))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + pos
    screen.blit(background, (0, 0))
    screen.blit(text, textpos)
    pygame.display.flip()

def afficherPDV(i, x, y, z, pos):
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render(i, 1, (x, y, z))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + pos
    screen.blit(text, textpos)
    pygame.display.flip()

#Affichage d'un texte centré sur deux lignes
def afficherText2l(i, j, x, y, z):
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

#Affichage des différents indicateur sous les photos    
def indicateur(photo):
    background.fill((255, 255, 255))
    font = pygame.font.Font(None, 30)
    text = font.render(('Codification souche : %s' % souche), 1, (255, 0, 255))
    text2 = font.render(('Nombre de spore : %s' % spore), 1, (255, 0, 255))
    text3 = font.render(('Surface du mycelium %s' % mycelium), 1, (255, 0, 255))
    text4 = font.render(('Serie n : %s' % shoot_nb), 1, (255, 0, 255))
    text5 = font.render(photo, 1, (255, 0, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery + 325
    text2pos = text.get_rect()
    text2pos.centerx = background.get_rect().centerx
    text2pos.centery = background.get_rect().centery + 350
    text3pos = text.get_rect()
    text3pos.centerx = background.get_rect().centerx
    text3pos.centery = background.get_rect().centery + 375
    text4pos = text.get_rect()
    text4pos.centerx = background.get_rect().centerx
    text4pos.centery = background.get_rect().centery + 300
    text5pos = text.get_rect()
    text5pos.centerx = background.get_rect().centerx
    text5pos.centery = background.get_rect().centery + 275
    screen.blit(background, (0, 0))
    screen.blit(text, textpos)
    screen.blit(text2, text2pos)
    screen.blit(text3, text3pos)
    screen.blit(text4, text4pos)
    screen.blit(text5, text5pos)

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()

#Incrémentation du numéro de shoot
shoot_nb += 1
serie = 'serie%i' % shoot_nb
try_serie = False
while try_serie != 'exit':
    serie = 'serie%i' % shoot_nb
    try:
        os.mkdir('%s/%s' % (dossier, serie))
    except:
        shoot_nb += 1
    else:
        try_serie = 'ex'
        
    try:
        os.mkdir('%s/%s' % (dossier_name, serie))
    except:
        pass
    else:
        try_serie = try_serie+'it'
          
#Choix nombre de photos a prendre
while exit_loop1 != 'yes': 
    '''choix3 = afficherText2l("Combien de photos souhaitez -vous prendre?", "Bouton joystick :5=5 6=10 7=15 8=20 9=25 10=30", 255, 0, 255) 
    print choix3'''
    for i in range(0,8):
        txt = afficherText("Combien de photos souhaitez -vous prendre?", 255, 0, 255, -200) 
        print txt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                i = evt.button
                frames = ((i-3)*5)
                      
                if frames == -15:
                    frames = 1
                    nb_frames = afficherText(("Vous avez choisi de prendre 1 photos"), 255, 0, 255, 0) 
                    print nb_frames
                    time.sleep(2)
                    exit_loop3 = 'yes'        
                if frames >=5 and frames <=30:
                    nb_frames = afficherText(("Vous avez choisi de prendre %i photos" % frames), 255, 0, 255, 0) 
                    print nb_frames
                    time.sleep(2)
                    exit_loop3 = 'yes'
                if evt.button == 11:
                    exit = afficherText("Fin du programme", 255, 0, 255, 0)
                    print exit
                    time.sleep(1)
                    sys.exit()
                else:
                    pass
                
            else:
                pass
#Prise de vue    
for i in range(0, frames):
    
    
    
    filename = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
    
    source_capture = filename
    camera.capture_image(source_capture)
    dest_capture = ('%s/%s' % (dossier, serie))
    
    shutil.move(source_capture, dest_capture)

    with Image(filename='%s/%s' % (dest_capture, filename)) as img:
            with img.clone() as j:
                j.resize((800), (600))              
                j.save(filename='%s/%s/%s' % (dossier_name, serie, filename))

    image_name = '%s%s-%i.jpg' % (photos_name, shoot_nb, i)
    image = pygame.image.load('%s/%s/%s' % (dossier_name, serie, image_name))
    screen.blit(background, (0, 0))
    screen.blit(image, (0,0))
    afficherPDV(("Photos prisent : %i/%i" % (i+1, frames)), 255, 0, 255, 300)
    pygame.display.update()
    time.sleep(interval)

    for evt in evts:
        if evt.type == pygame.locals.KEYDOWN:
            if evt.key == 27:
                exit = afficherText("Fin du programme", 255, 0, 255, 0)
                print exit
                time.sleep(1)
                sys.exit()

camera.exit()

#Stack les photos basse qualité pour un rendu rapide
cmd2 = 'enfuse -o %s%i.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/%s/*.jpg && mv %s%i.jpg %s/%s' % (image_fs, shoot_nb, dossier_name, serie, image_fs, shoot_nb, dossier_name, serie)
subprocess.check_output(cmd2, shell=True)
#Defilement manuel des photos
i = 0
if defil == 'Manuel':
    go = afficherText("Utilisez le HAT du Joystick pour faire defiler les photos", 255, 0, 255, 0)
    print go
        
    while True: 
        evts = pygame.event.get()
        if len(evts) > 0:
            for evt in evts:
                if evt.type == pygame.locals.JOYHATMOTION:
                    if evt.value[0] == -1 and evt.value[1] == 0:
                        if i >0:
                            i -= 1
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            image_name = '%s%i-0.jpg' % (photos_name, shoot_nb)
                            
                    elif evt.value[0] == 1 and evt.value[1] == 0:
                        if i <(frames-1):
                            i += 1
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
      
                            i = (frames-1)
                            image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        
                    elif evt.value[0] == 0 and evt.value[1] == 1:
                        if shoot_nb > 0:
                            shoot_nb -= 1
                            serie = 'serie%i' % shoot_nb
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            image_name = '%s%i-0.jpg' % (photos_name, shoot_nb)
                            
                    elif evt.value[0] == 0 and evt.value[1] == -1:
                        exist = os.path.exists('/media/snapcop/new/snapcop_adrien/%s/%s' % ((dossier_name, 'serie%i'% (shoot_nb + 1))))
                        if exist:
                            shoot_nb += 1
                            serie = 'serie%i' % shoot_nb
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        else:
                            serie = 'serie%i' % shoot_nb
                            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
                        
                        
                    else:
                    
                        image_name = '%s%s-%i.jpg' % (photos_name, shoot_nb, i)
                    image = pygame.image.load('%s/%s/%s' % (dossier_name, serie, image_name))
                    indicateur(('Photo : %s%i-%i' % (photos_name, shoot_nb, i)))
                    screen.blit(image, (0,0))
                    pygame.display.update()
                    time.sleep(0.3)
                
                if evt.type == pygame.locals.JOYBUTTONDOWN:
                    if evt.button == 1:
                        image_name = '%s%i.jpg' % (image_fs, shoot_nb)
                        indicateur('Photo : %s%i' % (image_fs, shoot_nb))
                        image = pygame.image.load('%s/%s/%s' % (dossier_name, serie, image_name))
                        screen.blit(image, (0,0))
                        pygame.display.update()
                
                if evt.type == pygame.locals.JOYBUTTONDOWN:
                    if evt.button == 11:
                        exit = afficherText("Fin du programme", 255, 0, 255, 0)
                        print exit
                        time.sleep(1)
                        sys.exit()
                        
                    
                
                else:
                    pass                
#Défilement automatique des photos
elif defil == 'Automatique':
    while True:
        for i in range(0,(frames)):
            image_name = '%s%i-%i.jpg' % (photos_name, shoot_nb, i)
            image = pygame.image.load('%s/%s/%s' % (dossier_name, serie, image_name))
            indicateur('Photo : %s%i-%i' % (photos_name, shoot_nb, i))
            screen.blit(image, (0,0))
            pygame.display.update()
            time.sleep(0.5)
            evts = pygame.event.get()
            if len(evts) > 0:
                for evt in evts:
                    if evt.type == pygame.locals.KEYDOWN:
                        if evt.key == 27:
                            exit = afficherText("Fin du programme", 255, 0, 255, 0)
                            print exit
                            time.sleep(1)
                            sys.exit()
                        else: 
                            pass
        final = pygame.image.load(('%s/%s/%s%i.jpg') % (dossier_name, serie, image_fs, shoot_nb))
        indicateur('Photo : %s%i' % (image_fs, shoot_nb))
        screen.blit(final, (0,0))
        pygame.display.update()
        background.fill((255, 255, 255))
        time.sleep(2)
        
#Message d'érreur        
elif choix == 'e':
    bad = afficherText("Votre choix n'est pas correct ! Relancez le script", 255, 0, 255, 0)
    print bad
    time.sleep(2)
    sys.exit()
    
else:
    pass
