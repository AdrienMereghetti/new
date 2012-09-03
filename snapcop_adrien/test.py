# -*- coding: utf-8 -*-

import sys, os, time
from datetime import date
import datetime

day = time.strftime("%d-%m-%Y", time.localtime())
dat ='15-08-2012'  
'''d0 = date(int(day[6:]), int(day[3:5]), int(dat[:2]))
d1 = date(int(dat[6:]), int(dat[3:5]), int(dat[:2]))
delta = d0 - d1
print delta.days'''

a = date(int(day[6:]), int(day[3:5]), int(dat[:2]))
b = date(int(dat[6:]), int(dat[3:5]), int(dat[:2]))
delta = a - b
datetime.timedelta(7)
print delta.days
