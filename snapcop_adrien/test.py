# -*- coding: utf-8 -*-

import usb, sys, os, time, subprocess
import pygame
from pygame.locals import *

'''for i in range(0, 8):
    cmd = 'cd Test_%i; mkdir rendu%i; for j in Test_%i*.jpg; do convert -quality 50 -resize 800x600 "$j" "rendu/$j"; done; mv rendu%i ..; cd .. ' % (i, i, i, i)
    cmd2 = 'enfuse -o Final_%i.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask rendu%i/*.jpg && mv Final_%i.jpg %s' % (i, i, i)
    subprocess.check_output(cmd, shell=True)
    subprocess.check_output(cmd2, shell=True)'''
    
'''busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        print
pygame.display.init()
window = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('Visu photo stacker 10/08/12')
screen = pygame.display.get_surface()
       
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

busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        idVendor = "0x%04x" % dev.idVendor
        idProduct = "0x%04x" % dev.idProduct
        if idVendor == '0x04a9' and idProduct == 0x31ea:
            camera_found = afficherText("L'appareil photo est connecté, 255, 0, 255")
            print camera_found
            print up'''
            
import re
import subprocess
device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb", shell=True)
devices = []
for i in df.split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)
print devices
