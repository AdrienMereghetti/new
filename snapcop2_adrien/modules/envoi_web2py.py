#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import redis
import shutil
import sys
import time
from wand.image import Image

def main():
    cx = redis.Redis()
    ps = cx.pubsub()
    ps.subscribe(['envoi', 'exit'])
    for m in ps.listen():
        data = str(m['data'])
        if data[:3] == 'sys':
                sys.exit()
        print 'Envoi!'
        frames = int(cx.get('frames'))
        # On récupère les x dernières photos
        serie = cx.lrange('captures', -frames, -1)
        for i in range(0, frames):
            dest = '../web2py/applications/snapcop2_web2py/static/Photos'
            shutil.copy2(serie[i], dest)
            short_name = os.path.split(serie[i])[1]
            photo_envoi = '/snapcop2_web2py/static/Photos/%s'%short_name
            cx.rpush('photo_envoi', photo_envoi)
            image = serie[i]
            image='%s/%s'%(dest, image[-22:])
            thumb='%sthumb%s'% (image[:-22], image[-18:])
            short_thumb = os.path.split(thumb)[1]
            thumb_envoi = '/snapcop2_web2py/static/Photos/%s'%short_thumb
            cx.rpush('thumb_envoi', thumb_envoi)
            with Image(filename = image) as img:
                with img.clone() as i:
                    i.resize((800), (533))
                    i.save(filename=thumb)
            os.remove(image) 
