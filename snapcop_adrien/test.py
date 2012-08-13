# -*- coding: utf-8 -*-

import usb, sys, os, time, subprocess
import pygame
from pygame.locals import *
pygame.display.init()
pygame.joystick.init()

cmd = 'mkdir output; for i in *.jpg; do convert -resize 800x600 -quality 50 "$i" "output/$i"; done'
subprocess.check_output(cmd, shell=True)
