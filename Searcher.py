# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:06:36 2020

@author: Florencia
"""
import mysql.connector

class Pokesearch:
    def __init__(self):
        self.db = mysql.connector.connect(host="localhost",user="root",
                               password="Alemania06", database='sql_pokemon')
    def searchPkmn(self,pokemon):
        cursor=self.db.cursor()
        sentence = '''SELECT poke.pok_id, poke.pok_name, poke.pok_height, poke.pok_weight, ty.type_name
                FROM pokemon poke
                JOIN pokemon_types pt
            	USING(pok_id)
                JOIN types ty
                USING(type_id)
                WHERE pok_name = "{}"'''.format(pokemon)
        cursor.execute(sentence)
        return self.info(pokemon,cursor)
    def close_con(self):
        self.db.close()
        
    def info(self,pokemon,cursor):
        res=""
        currPokemon=""
        for id, name, height, weight,type in cursor:
            if currPokemon != name:
                res=res[:-1]
                res += "ID: " + str(id) + "\n Height: " + str(height) +"\n Weight: " + str(weight)+"\nType/s: " 
            res+= str(type)+"/"
            currPokemon = name
        res=res[:-1]
        cursor.close()
        return str(pokemon) + ": \n" + res
