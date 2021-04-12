# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:29:02 2020

@author: Florencia
"""
import mysql.connector
from tkinter import *

def search_pokemon(pokemon):
    #Busco en la base de datos
    sentence = '''SELECT poke.pok_id, poke.pok_name, poke.pok_height, poke.pok_weight, ty.type_name
                FROM pokemon poke
                JOIN pokemon_types pt
            	USING(pok_id)
                JOIN types ty
                USING(type_id)
                WHERE pok_name = "{}"'''.format(pokemon)
    mycursor.execute(sentence)
    res=""
    currPokemon=""
    for id, name, height, weight,type in mycursor:
        if currPokemon!=name:
            res=res[:-1]
            res += "ID: " + str(id) + "\n Height: " + str(height) +"\n Weight: " + str(weight)+"\nType/s: " 
        res+= str(type)+"/"
        currPokemon=name
    res=res[:-1]
    return str(pokemon) + ": \n" + res
    
    
def clicked():
    res = search_pokemon(input_poke.get())
    lbl.configure(text= res)

#MAIN#

#Me conecto a la base de datos
mydb = mysql.connector.connect(host="localhost",user="root",
                               password="Alemania06", database='sql_pokemon')
#Creo el cursor
mycursor = mydb.cursor()

#Creo la interfaz gráfica
root = Tk()
root.title("Buscador pokemon")
root.geometry('350x200') 

input_poke = Entry(root, width = 50)
input_poke.grid(column=0, row=0)

lbl = Label(root, text= "")
lbl.grid(column=0, row=3)

search_button = Button(root, text="Buscar", command = clicked)
search_button.grid(column=1, row=0)

root.mainloop()

#Cierro la base de datos
mycursor.close()        
mydb.close()