# -*- coding: utf-8 -*-

import time
import redis
cx = redis.Redis()


def toto():
  # cx redis
  x = cx.get('joyx')
  y = cx.get('joyy')
  return locals()

# approche "webserver"
# une page web appel "très rapidment" le serveur
  
while True:
  time.sleep(1.0)
  print toto()
