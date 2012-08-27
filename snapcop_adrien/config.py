# -*- coding: utf-8 -*-
import time, redis
day = time.strftime("%d-%m-%Y", time.localtime())
cx = redis.Redis()

dossier = '%s-%s' % ((str(cx.get('dossier'))), day)
dossier_name = '%s-%s' % ((str(cx.get('dossier_name'))), day)
image_fs = '%s_'%(str(cx.get('image_fs')))
interval = int(cx.get('interval'))
photos_name = '%s_'%str(cx.get('photos_name'))
souche = str(cx.get('souche'))
