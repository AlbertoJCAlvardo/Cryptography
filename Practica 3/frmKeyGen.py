from tkinter import *
from inicial import Inicial


class frmKeyGen(Frame):
    
              
    def __init__(self, master):
        Frame.__init__(self, master)
        opcion = IntVar()
        import os
        self.dire = os.getcwd()
        Frame.configure(self,bg="#A8DADC")
        self.ltitulo = Label(self, text="Generador de Llaves", font=('Palatino', 50), bg="#A8DADC", 
                             fg = "#1d3557").grid(row=0, column=1,padx=50, pady=50)
        self.lName = Label(self, text="Nombre: ", font=('Palatino', 25), bg="#A8DADC", 
                             fg = "#1d3557").grid(row=1, column=0,padx=10, pady=10)
        self.entName = Entry(self, width=25)
        self.op1 = Button(self, text="Generar Llave  ", font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",       
                  command=lambda: self.generarLlave()).grid(row=2,column=1, padx=10, pady=15)
        self.op1 = Button(self, text="Volver", font=('Georgia', 15), bg = "#19535F", fg = "#A8DADC",       
                          command=lambda: master.switchFrame(Inicial)).grid(row=2,column=2, padx=10, pady=15)
        self.entName.grid(row=1, column=1,padx=10, pady=10)
        
    def limpiarDirectorio(self, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
        
    def generarLlave(self):
            
            import rsa
            import os
            import binascii
            from tkinter import messagebox as MessageBox
            nombre = self.entName.get()
            
            ruta = self.dire
            
        
             
            from Cryptodome.PublicKey import RSA
            
            key = RSA.generate(2048)
        
            private_key = key.export_key(format="DER")
            private_key = binascii.hexlify(private_key).decode(encoding='utf-8')
            
            file_out = open(nombre+" Llave Privada.txt", "w")
            file_out.write(private_key)
            file_out.close()

            public_key = key.publickey().export_key(format="DER")
            public_key = binascii.hexlify(public_key).decode(encoding='utf-8')
            file_out = open(nombre+" Llave Publica.txt", "w")
            file_out.write(public_key)
            file_out.close() 
            MessageBox.showinfo("","Llaves generadas con éxito")
    
    