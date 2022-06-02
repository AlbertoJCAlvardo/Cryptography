from tkinter import*
from frmCifrar import *
from frmDescifrar import *

class Aplicacion(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Cifrado DES")
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
        self.ltitulo = Label(self, text="Práctica 2:\nCifrado DES\nMenú", font=('Palatino', 50), bg="#A8DADC", 
                             fg = "#1d3557").grid(row=0, column=1,padx=100, pady=50)
        self.l1 = Label(self, text="Opciones: ", font=('Palatino', 30), bg="#A8DADC", 
                             fg = "#1d3557").grid(row=1, column=0,padx=10, pady=10)
        self.op1 = Button(self, text="  Cifrar  ", font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",       
                  command=lambda: master.switchFrame(frmCifrar)).grid(row=2,column=1, padx=10, pady=15)
        
        self.op2 = Button(self, text="Descifrar",  font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",        

                         command=lambda: master.switchFrame(frmDescifrar)).grid(row=2, column=2, padx=10, pady=15)