# -*- coding: utf-8 -*-

import pygame, sys, os, time
from pygame.locals import * 

import redis

pygame.init()
pygame.joystick.init()

cx = redis.Redis()

try:
    stick = pygame.joystick.Joystick(0)
    stick.init()
    print 'joystick trouvé !'
except:
    print 'pas de joystick !!'
    sys.exit()

x, y, a, b, c, d, e, f = 0, 0, 200, 0, 400, 0, 0, 200  

cx.set('c', c)
cx.set('d', d)
cx.set('e', e)
cx.set('f', f)
cx.publish('c1', c)
cx.publish('c1', d)
cx.publish('c1', e)
cx.publish('c1', f)
while True: 
    evts = pygame.event.get()
    if len(evts) > 0:
        for evt in evts:
            #Mouvement des axes + Gachettes
            if evt.type == pygame.locals.JOYAXISMOTION:
                #Joystick Gauche = Angry bird rouge
                if evt.axis == 0:
                    print 'joy axis motion', evt.axis, evt.value
                    x = int((evt.value + 1.0) * 300)
                    if x > 600:
                        x = 600
                    cx.set('x', x)
                    cx.publish('c1', x)
                    
                elif evt.axis == 1:
                    print 'joy axis motion', evt.axis, evt.value
                    y = int((evt.value + 1.0) * 200)
                    if y > 400:
                        y = 400
                    cx.set('y', y)
                    cx.publish('c1', y)
                #Joystick Droite = Pig    
                elif evt.axis == 3:
                    a = int((evt.value + 1.0) * 300)
                    if a > 600:
                        a = 600
                    cx.set('a', a)
                    cx.publish('c1', a)
                    
                elif evt.axis == 4:
                    b = int((evt.value + 1.0) * 200)
                    if b > 400:
                        b = 400
                    cx.set('b', b)
                    cx.publish('c1', b)
                #Gachette Gauche/Droite = Angry bird vert        
                elif evt.axis == 2:
                    e = int((evt.value + 1.0) * 300)
                    if e > 600:
                        e = 600
                    cx.set('e', e)
                    cx.publish('c1', e)
                    
                elif evt.axis == 5:
                    f = int((evt.value + 1.0) * 200)
                    if f > 400:
                        f = 400
                    cx.set('f', f)
                    cx.publish('c1', f)
            #Mouvement du black bird grâce au HAT        
            elif evt.type == pygame.locals.JOYHATMOTION:
                if evt.value[0] == -1 and evt.value[1] == 0:
                    c -= 10
                    if c < 0:
                        c = 0
                    cx.set('c', c)
                    cx.publish('c1', c)
                
                elif evt.value[0] == 1 and evt.value[1] == 0:
                    c += 10
                    if c > 600:
                        c = 600
                    cx.set('c', c)
                    cx.publish('c1', c)
                    
                elif evt.value[0] == 0 and evt.value[1] == 1:
                    d -= 10
                    if d < 0:
                        d = 0
                    cx.set('d', d)
                    cx.publish('c1', d)
                        
                elif evt.value[0] == 0 and evt.value[1] == -1:
                    d += 10
                    if d > 400:
                        d = 400
                    cx.set('d', d)
                    cx.publish('c1', d)
            
            else:
                pass
                        
