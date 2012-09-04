import redis

def thumb():
    """
    Renvoie dans photos la liste des x dernières photos prises
  
    """
    # connexion redis
    # récupérer le nb de photo prises (GET frames)
    # récupérere la liste des chemins des photos (LRANGE -5 -1)

    cx=redis.Redis()
    frames = int(cx.get('frames'))
    photos = cx.lrange('photo_envoi', -frames, -1)
    thumbs = cx.lrange('thumb_envoi', -frames, -1)
    stack = cx.get('Stack')
    souche = 'Souche : %s'%str(cx.get('souche'))
    substrat = 'Substrat : %s'%str(cx.get('substrat'))
    fermentation = 'Durée de fermentation : %s jours'%str(cx.get('fermentation'))
    stacking = 'Stack %s'%souche
    spore = 'Nombre de spores : 0'
    mycelium = 'Surface du mycelium : 0'
    auteur = 'None'
    return locals()
