#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis

cx=redis.Redis()
serie = cx.lrange('captures', -2, -1)
print serie
