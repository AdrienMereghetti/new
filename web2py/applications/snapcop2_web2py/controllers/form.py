# -*- coding: utf-8 -*-

import redis
cx = redis.Redis()


def first():
    form=FORM(TABLE(TR("Codification souche:",INPUT(_type="text",_name="souche",requires=IS_NOT_EMPTY())),
                    TR("Substrat:",INPUT(_type="text",_name="substrat",requires=IS_NOT_EMPTY())),
                    TR("Durée de fermentation:",INPUT(_type="text",_name="fermentation",requires=IS_INT_IN_RANGE(0, 9999))),
                    TR("Commentaires",TEXTAREA(_name="profile",value="Commentaire ici")),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.accepts(request,session):
        response.flash="Formulaire accepté"
    elif form.errors:
        response.flash="Formulaire invalide"
    else:
        response.flash="Remplissez le formulaire"
    souche = str(request.vars.souche)
    substrat = str(request.vars.substrat)
    fermentation = str(request.vars.fermentation)
    cx.publish('souche', souche)
    cx.publish('substrat', substrat)
    cx.publish('fermentation', fermentation)
    return dict(form=form,vars=form.vars)
