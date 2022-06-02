from tkinter import *

from frmCifrar import frmCifrar
from frmDescifrar import  frmDescifrar
from frmKeyGen import frmKeyGen

class Aplicacion(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Cifrado RSA")
        self.geometry("900x600")
        self.config(bg="#A8DADC")
        self.frm = None
        self.switchFrame(Inicial)
        
        self.mainloop()
        
    def switchFrame(self , n_frame):
        fr = n_frame(self)
        if self.frm is not None:
            self.frm.destroy()
        self.frm = fr
        self.frm.pack()
    
    

class Inicial(Frame):
    
              
    def __init__(self, master):
        Frame.__init__(self, master)
        opcion = IntVar()
        self.config(bg="#A8DADC", height="600", width ="800")
        self.ltitulo = Label(self, text="Práctica 3:\nCifrado RSA\nMenú", font=('Palatino', 50), bg="#A8DADC", 
                             fg = "#1d3557").grid(row=0, column=1,padx=100, pady=50)
        self.l1 = Label(self, text="Opciones: ", font=('Palatino', 30), bg="#A8DADC", 
                             fg = "#1d3557").grid(row=1, column=0,padx=10, pady=10)
        self.op1 = Button(self, text="  Cifrar  ", font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",       
                  command=lambda: master.switchFrame(frmCifrar))
        
        self.op2 = Button(self, text="Descifrar",  font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",        

                         command=lambda: master.switchFrame(frmDescifrar))
        self.op3 = Button(self, text="Generar Llaves",  font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",        

                         command=lambda: master.switchFrame(frmKeyGen))
        self.op1.grid(row=2,column=1, padx=10, pady=15)
        self.op2.grid(row=2, column=2, padx=10, pady=15)
        self.op3.grid(row=3, column=1, padx=10, pady=15)
        