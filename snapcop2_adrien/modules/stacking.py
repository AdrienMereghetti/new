#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import redis
import shutil
import subprocess
import time



def main(lent):
    
    # connection redis
    cx = redis.Redis()
    day = time.strftime("%d-%m-%Y", time.localtime())
    
    shoot_nb = int(cx.get('shoot'))
    
    canal = 'stack_lent' if lent else 'stack_rapide'
    
    
    
    # attente d'une publication
    ps = cx.pubsub()
    ps.subscribe([canal])
    for m in ps.listen():
        frames = int(cx.get('frames'))
        # On récupère les x dernières photos
        serie = cx.lrange('captures', -frames, -1)
        dest_stack = 'data/stack_lent'
        
        shoot_nb += 1
        cx.set('shoot', shoot_nb)
        
        series = 'serie%s' % shoot_nb
        try:
            os.mkdir('%s/%s'%(dest_stack, series))
        except:
            pass
            
        for i in range(0, frames):
            shutil.copy2(serie[i], '%s/%s'%(dest_stack, series))
        
        
        
        for i in range(0, frames):
            fichier = open("fichier.txt", "a")
            fichier.write('%s, serie%i, %s\n' % (day, shoot_nb, serie[i]))         
            fichier.close()
        
        # execution de stack
        
        cmd = 'enfuse -o Stack%i.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/%s/*.jpg' % (shoot_nb, dest_stack, series)
        subprocess.check_output(cmd, shell=True)
        shutil.move('Stack%i.jpg' % shoot_nb, '%s/%s'% (dest_stack, series))
        
        stack = '%s/%s/Stack%i.jpg' % (dest_stack, series, shoot_nb)
        # publication stacking terminé
        cx.publish('stacking', stack)
        frames = 0
        cx.set('frames', frames)
        print 'Finish !!'
