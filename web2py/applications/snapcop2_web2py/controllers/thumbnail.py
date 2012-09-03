import redis

def thumb():
    cx=redis.Redis()
    frames = int(cx.get('frames'))
    image=[]
    serie = cx.lrange('captures', -frames, -1)
    
    for i in range(0, frames):
        photo = serie[i]
        image+=[
        A(IMG(_src=URL('static/Photos', 'thumb%s'%photo[-18:]), _alt="Capt"),
                  _href=URL('static/Photos', photo[-22:])),
              ]
    return dict(image=image)
