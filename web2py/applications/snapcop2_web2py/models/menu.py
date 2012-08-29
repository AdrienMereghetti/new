# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('Snapcop2 : Prise de vue Stacking auto')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'Prises de vue automatique'
response.meta.keywords = 'web2py, python, framework, snapcop, photo'
response.meta.generator = 'Snapcop'
response.meta.copyright = 'Copyright 2012'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu+=[
        (SPAN('Snapcop2',_style='color:magenta'),False, None, [
                (T('Prise de vue'),False,URL('form', 'info')),
                (T('Prise de vue Eric'),False,URL('prise_de_vue', 'Config')),
                (T('Prise de vue Eric2'),False,URL('prise_de_vue5', 'Config'))
                        
                
                        ])
                ]
_()

