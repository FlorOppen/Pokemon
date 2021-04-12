# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:29:02 2020

@author: Florencia
"""
import mysql.connector
from tkinter import *

def search_pokemon(pokemon):
    #Me conecto a la base de datos
    mydb = mysql.connector.connect(host="localhost",user="root",
                                   password="Alemania06", database='sql_pokemon')
    #Creo el cursor
    mycursor = mydb.cursor()
    #Busco en la base de datos
    sentence = '''SELECT pok_id, pok_name, pok_height, pok_weight 
                FROM pokemon
                WHERE pok_name = "{}"'''.format(pokemon)
    mycursor.execute(sentence)
    
    for id, name, height, weight in mycursor:
        res = "ID: " + str(id) + "\n Altura: " + str(height) +"\n Peso: " + str(weight)
    mycursor.close()        
    mydb.close()
    return str(pokemon) + ": \n" + res
    
    

#charizarprint(search_pokemon("charizard"))

def clicked():
    res = search_pokemon(input_poke.get())
    lbl.configure(text= res)

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
