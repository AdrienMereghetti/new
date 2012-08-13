# -*- coding: utf-8 -*-

import usb, sys, os, time, subprocess
import pygame
from pygame.locals import *
pygame.display.init()
pygame.joystick.init()

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()
    
while True:
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            if evt.type == pygame.locals.JOYBUTTONDOWN:
                i = evt.button
                frames = ((i-3)*5)
                print frames
