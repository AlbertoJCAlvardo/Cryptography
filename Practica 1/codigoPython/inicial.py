from tkinter import *
from cifradores import *



class Inicial(Frame):
    
              
    def __init__(self, master):
        Frame.__init__(self, master)
        opcion = IntVar()
        self.config(bg="#564256", height="600", width ="800")
        self.ltitulo = Label(self, text="Práctica 1\nMenú", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8").grid(row=0, column=1,padx=100, pady=50)
        self.l1 = Label(self, text="Opciones: ", font=('Chiller', 30), bg="#564256", 
                             fg = "#E8E8E8").grid(row=1, column=0,padx=10, pady=10)
        self.op1 = Radiobutton(self, text="Affine",font=('Chiller', 30), bg = "#564256", variable=opcion, fg = "#E8E8E8"
                               ,value=1).grid(row=1, column=1, padx=10, pady =10,sticky="nw")
        
        self.op2 = Radiobutton(self, text="Vigènere",font=('Chiller', 30), bg = "#564256", fg = "#E8E8E8",
                               variable=opcion, value=2).grid(row=2, column=1, padx=10, pady =10,sticky="nw")
        
        self.opk = Button(self, text="       Ir     ", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",        
                  command=lambda: master.transportar(opcion.get())).grid(row=2, column=2, padx=10, pady=15)

    
            
    
