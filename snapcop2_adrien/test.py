#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pyexiv2, time


'''exif=True
while exif:
    for i in range(0, 1):
        metadata = pyexiv2.ImageMetadata('test.jpg')
        metadata.read()
        tag = metadata['Exif.Photo.UserComment']
        key = 'Exif.Photo.UserComment'
        value = ['Air', 'Air']
        metadata[key] = value [i]
        metadata.write()
        metadata.read()
        exif=False
print tag.value'''

metadata = pyexiv2.ImageMetadata('test.jpg')
metadata.read()
pyexiv2.xmp.register_namespace('Souche/', 'Souche')
pyexiv2.xmp.register_namespace('Auteur/', 'Auteur')
pyexiv2.xmp.register_namespace('Description/', 'Description')
metadata['Xmp.Souche.Souche'] = 'Nothing'
metadata['Xmp.Auteur.Auteur'] = 'Adrien'
metadata['Xmp.Description.Description'] = 'Capuchon de clef USB'
tag = metadata['Xmp.Souche.Souche']
tag2 = metadata['Xmp.Auteur.Auteur']
tag3 = metadata['Xmp.Description.Description']
print tag.value
print tag2.value
print tag3.value
