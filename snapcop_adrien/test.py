# -*- coding: utf-8 -*-

import usb, sys, os, time, subprocess
import pygame
from pygame.locals import *
pygame.display.init()
pygame.joystick.init()

day = time.strftime("%d-%m-%Y", time.localtime())
dossier = 'shoot-%s' % day
dossier_name = 'rendu-%s' % day
shoot_nb = 0

exist = os.path.exists('/media/snapcop/new/snapcop_adrien/rendu-17-08-2012/')

print type(exist)



