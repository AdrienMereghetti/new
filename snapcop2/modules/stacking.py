#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis
import time

def main(lent):
    canal = 'stack_lent' if lent else 'stack_rapide'
    
    # connection redis
    cx = redis.Redis()
    
    # attente d'une publication
    ps = cx.pubsub()
    ps.subscribe([canal])
    for m in ps.listen():
        # On récupère les x dernières photos
        print cx.lrange('captures', -5, -1)
        
        # execution de stack
        time.sleep(5)
        
        # publication stacking terminé
        cx.publish('stacking', 'done')
