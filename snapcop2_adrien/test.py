#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis

cx = redis.Redis()
pubsub = cx.pubsub()  
pubsub.subscribe(['capture', 'stacking'])
for m in pubsub.listen():
    data = str(m['data'])
    if data[:6] == 'data/i':
        capture = m['data']    
        print capture
    elif data[:6] == 'data/s':
        capture = m['data']    
        print capture
