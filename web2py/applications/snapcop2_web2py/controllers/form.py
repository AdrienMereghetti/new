# -*- coding: utf-8 -*-

import redis
import pygame
from pygame.locals import *
cx = redis.Redis()


def info():
    form=FORM(TABLE(TR("Codification souche:",INPUT(_type="text",_name="souche",value="O26",requires=IS_NOT_EMPTY())),
                    TR("Substrat:",INPUT(_type="text",_name="substrat",value="Nope",requires=IS_NOT_EMPTY())),
                    TR("Durée de fermentation:",INPUT(_type="text",_name="fermentation",value="10",requires=IS_INT_IN_RANGE(0, 9999))),
                    TR("Commentaires",TEXTAREA(_name="Commentaire",value="Commentaire ici")),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.accepts(request,session):
        response.flash="Formulaire accepté"
        souche = str(request.vars.souche)
        substrat = str(request.vars.substrat)
        fermentation = str(request.vars.fermentation)
        cx.set('souche', souche)
        cx.set('substrat', substrat)
        cx.set('fermentation', fermentation)
        #redirect(URL(request.application, 'capture', 'capture'))
        return dict(form=form, vars=form.vars)
    elif form.errors:
        response.flash="Formulaire invalide"
    else:
        response.flash="Remplissez le formulaire"
    return dict(form=form)
