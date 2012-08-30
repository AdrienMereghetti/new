# -*- coding: utf-8 -*-
import os


try_serie = '' 
while try_serie != 'exit':
    try:
        os.mkdir('serie1')
    except:
        print 'except'
    else:
        try_serie = 'ex'
        
    try:
        os.mkdir('serie2')
    except:
        print 'except2'
    else:
        try_serie += 'it'
    
print try_serie
