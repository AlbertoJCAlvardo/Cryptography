# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:12:17 2020

@author: argen"""


from inicial import *
from tkinter import*
from cifradores import *


class Aplicacion(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Programa de Cifrado")
        self.geometry("800x600")
        self.config(bg="#564956")
        self.frm = None
        self.switchFrame(Inicial)
        
        self.mainloop()
        
    def switchFrame(self , n_frame):
        fr = n_frame(self)
        if self.frm is not None:
            self.frm.destroy()
        self.frm = fr
        self.frm.pack()
    def transportar(master, op):
        if op == 1:
             master.switchFrame(frmAffine)
        if op == 2:
             master.switchFrame(frmVig)

        

app = Aplicacion()