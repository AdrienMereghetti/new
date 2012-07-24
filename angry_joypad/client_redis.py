# -*- coding: utf-8 -*-

import redis
cx = redis.Redis()

pubsub = cx.pubsub()
  
pubsub.subscribe(['c1'])
for m in pubsub.listen():
    x = cx.get('joyx') 
    y = cx.get('joyy')  
    print x
    

