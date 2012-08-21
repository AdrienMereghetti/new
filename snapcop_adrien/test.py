# -*- coding: utf-8 -*-

import usb, sys, os, time, subprocess
from wand.image import Image
from wand.display import display

with Image(filename='O26_9-0.jpg') as img:
    print img.size
    with img.clone() as i:
        i.resize((800), (600))
        i.save(filename='O26_9-0.jpg')
        display(i)
