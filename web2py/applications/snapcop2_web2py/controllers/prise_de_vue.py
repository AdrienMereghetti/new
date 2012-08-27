# -*- coding: utf-8 -*-

import redis
import pygame
from pygame.locals import *
cx = redis.Redis()


def Config():
    form=FORM(TABLE(TR('Nom du dossier des photos "lourdes" : ',INPUT(_type="text",_name="dossier",value="shoot",requires=IS_NOT_EMPTY())),
                    TR('Nom du dossier des photos compréssé : ',INPUT(_type="text",_name="dossier_name",value="rendu",requires=IS_NOT_EMPTY())),
                    TR('Nom de la photo stacké : ',INPUT(_type="text",_name="image_fs",value="Final",requires=IS_NOT_EMPTY())),
                    TR('Inrterval de temps entre deux prise de vue (sec) : ',INPUT(_type="text",_name="interval",value="4",requires=IS_INT_IN_RANGE(0, 20))),
                    TR('Nom des photos : ',INPUT(_type="text",_name="photos_name",value="Capuchon",requires=IS_NOT_EMPTY())),
                    TR('Nom de la souche : ',INPUT(_type="text",_name="souche",value="Capuchon clef USB",requires=IS_NOT_EMPTY())),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.accepts(request,session):
        response.flash="Formulaire accepté"
        dossier = str(request.vars.dossier)
        dossier_name = str(request.vars.dossier_name)
        image_fs = str(request.vars.image_fs)
        interval = str(request.vars.interval)
        photos_name = str(request.vars.photos_name)
        souche = str(request.vars.souche)
        cx.set('dossier', dossier)
        cx.set('dossier_name', dossier_name)
        cx.set('image_fs', image_fs)
        cx.set('interval', interval)
        cx.set('photos_name', photos_name)
        cx.set('souche', souche)
        #redirect(URL(request.application, 'capture', 'capture'))
        return dict(form=form, vars=form.vars)
    elif form.errors:
        response.flash="Formulaire invalide"
    else:
        response.flash="Remplissez le formulaire"
    return dict(form=form)   
