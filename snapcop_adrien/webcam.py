# -*- coding: utf-8 -*-

import redis
import subprocess

cx = redis.Redis()
cx2 = redis.Redis()

pubsub = cx.pubsub()  
pubsub.subscribe(['sc:take_photo'])


while True:
    for m in pubsub.listen():
        nb_photo = int(m['data'])
        print '%i photos à prendre ...' % nb_photo
        
        cmd = 'gphoto2 --capture-image-and-download --force-overwrite --frames=%i --interval=2' % nb_photo
        subprocess.check_output(cmd, shell=True)
        
        cx2.publish('sc:photo_taken', 'capt0000.jpg')
