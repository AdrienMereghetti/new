#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis

cx = redis.Redis()
get = cx.get('souche')
get2 = cx.get('substrat')
get3 = cx.get('fermentation')
print 'Souche :', get
print 'Substrat :', get2
print 'Durée de fermentation :', get3
