# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:05:52 2020

@author: Florencia
"""
from tkinter import *
from Searcher import Pokesearch

 
class Interface:
    def __init__(self,pokesearch):
        self.root = Tk()
        self.root.title("Buscador pokemon")
        self.root.geometry('350x200')
        
        self.search_button = Button(self.root, text="Buscar", command = self.clicked)
        self.search_button.grid(column=1, row=0)
        
        self.lbl = Label(self.root)
        self.lbl.grid(column=0, row=3)    
        
        self.input_poke = Entry(self.root, width = 50)
        self.input_poke.grid(column=0, row=0)
        
        self.poke_search=pokesearch
        self.root.mainloop()        
    def clicked(self):
        res = self.poke_search.searchPkmn(self.input_poke.get())
        self.lbl.configure(text= res)
                    


        