# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

pygame.init()
pygame.joystick.init()
#Vérifie si un pad est branché
try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    
#Création de la fenetre
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Angry') 
screen = pygame.display.get_surface() 

#chargement des images
angryBird = pygame.image.load('./images/AngryBird.png')
angryBlackBird = pygame.image.load('./images/AngryBlackBird.png')
angryGreenBird = pygame.image.load('./images/AngryGreenBird.png')
angryPiggy = pygame.image.load('./images/AngryPiggy.png')
background = pygame.image.load('./images/Background.png')

#Initalisation de la position des images par défaut
x, y, a, b, c, d, e, f = 0, 0, 200, 0, 400, 0, 0, 200

while True: 
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            #Mouvement du black bird grâce au HAT
            if evt.type == pygame.locals.JOYHATMOTION:
                if evt.value[0] == -1 and evt.value[1] == 0:
                    c -= 10
                    if c < 0:
                        c = 0
                
                elif evt.value[0] == 1 and evt.value[1] == 0:
                    c += 10
                    if c > 600:
                        c = 600
                        
                elif evt.value[0] == 0 and evt.value[1] == 1:
                    d -= 10
                    if d < 0:
                        d = 0
                        
                elif evt.value[0] == 0 and evt.value[1] == -1:
                    d += 10
                    if d > 400:
                        d = 400
            #Mouvement des axes + Gachettes
            elif evt.type == pygame.locals.JOYAXISMOTION:
                #Joystick Gauche = Angry bird rouge
                if evt.axis == 0:
                    x = int((evt.value + 1.0) * 300)
                    if x > 600:
                        x = 600
                elif evt.axis == 1:
                    y = int((evt.value + 1.0) * 200)
                    if y > 400:
                        y = 400
                #Joystick Droite = Pig
                elif evt.axis == 3:
                    a = int((evt.value + 1.0) * 300)
                    if a > 600:
                        a = 600
                elif evt.axis == 4:
                    b = int((evt.value + 1.0) * 200)
                    if b > 400:
                        b = 400
                #Gachette Gauche/Droite = Angry bird rouge        
                elif evt.axis == 2:
                    e = int((evt.value + 1.0) * 300)
                    if e > 600:
                        e = 600
                elif evt.axis == 5:
                    f = int((evt.value + 1.0) * 200)
                    if f > 400:
                        f = 400
            #Echap pour quiter
            elif evt.type == pygame.locals.KEYDOWN:
                if evt.key == pygame.locals.K_ESCAPE:
                    print 'sortie ...'
                    sys.exit()
            else:
                pass
    #Affichage du Background et des Angry Birds   
    screen.blit(background, (0,0))
    screen.blit(angryBird, (x,y))
    screen.blit(angryGreenBird, (e,f))
    screen.blit(angryPiggy, (a,b))
    screen.blit(angryBlackBird, (c,d))
    pygame.display.update() 
      
