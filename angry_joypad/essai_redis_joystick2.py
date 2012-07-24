# -*- coding: utf-8 -*-

import redis
cx = redis.Redis()

pubsub = cx.pubsub()
  
pubsub.subscribe(['c1', 'c2'])
for m in pubsub.listen():
    print "From Redis:", m
