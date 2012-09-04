#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import redis
import shutil
import subprocess
import time
from wand.image import Image



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
        dest_stack = 'data/%s' % canal
        
        shoot_nb += 1
        cx.set('shoot', shoot_nb)
        
        series = 'serie%s' % shoot_nb
        try:
            os.mkdir('%s/%s'%(dest_stack, series))
        except:
            pass
            
        for i in range(0, frames):
            shutil.copy2(serie[i], '%s/%s'%(dest_stack, series))
            if canal == 'stack_rapide':
                image = serie[i]
                image='%s/%s/%s'%(dest_stack, series, image[-22:])
                with Image(filename = image) as img:
                    with img.clone() as i:
                        i.resize((800), (533))
                        i.save(filename=image)
                
                
        
        
        
        for i in range(0, frames):
            fichier = open("fichier.txt", "a")
            fichier.write('%s, serie%i, %s\n' % (day, shoot_nb, serie[i]))         
            fichier.close()
        
        # execution de stack
        
        cmd = 'enfuse -o Stack%i.jpg --exposure-weight=1 --saturation-weight=0.1 --contrast-weight=1 --exposure-sigma=0 --exposure-mu=1 --gray-projector=l-star --hard-mask %s/%s/*.jpg' % (shoot_nb, dest_stack, series)
        subprocess.check_output(cmd, shell=True)
        dest = '../web2py/applications/snapcop2_web2py/static/Photos'
        photo = 'Stack%i.jpg' %shoot_nb
        # envoi du résultat vers web2py
        shutil.copy2(photo, dest)
        # diminution de la résolution de la photo
        with Image(filename = photo) as img:
            with img.clone() as i:
                i.resize((800), (533))
                i.save(filename='%s/thumb%s'% (dest, photo))
        stack_envoi = '/snapcop2_web2py/static/Photos/%s'%photo
        
        thumb='%s/thumb%s'% (dest, photo)
        print 'thumb', thumb
        short_thumb = os.path.split(thumb)[1]
        print 'short', short_thumb
        thumb_envoi = '/snapcop2_web2py/static/Photos/%s'%short_thumb
        print 'stackenvoi', stack_envoi
        cx.set('Stack', thumb_envoi)
        
        shutil.move('Stack%i.jpg' % shoot_nb, '%s/%s'% (dest_stack, series))
        
        stack = '%s/%s/Stack%i.jpg' % (dest_stack, series, shoot_nb)
        print 'stack',stack
        # publication stacking terminé
        cx.publish('stacking', stack)
        #frames = 0
        #cx.set('frames', frames)
        remove = '%s/Stack%i.jpg'%(dest, shoot_nb)
        os.remove(remove)
        
        print 'Finish !!'
