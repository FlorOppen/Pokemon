# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:07:44 2020

@author: Florencia
"""
from Interface import Interface
from Searcher import Pokesearch

pokesearch=Pokesearch()
interfaz = Interface(pokesearch)

#Cierro el cursor y la base de datos
#mycursor.close()        
#mydb.close()