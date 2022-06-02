from tkinter import *
from inicial import Inicial

from Cryptodome.Cipher import DES

class frmDescifrar(Frame):
    def __init__(self, master):
        import os
        opcion = IntVar()
        self.dire = os.getcwd()
        Frame.__init__(self, master)
        Frame.configure(self,bg="#A8DADC")
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Descifrar", font=('Palatino', 50), bg="#A8DADC", 
                             fg = "#1d3557")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command = self.leerArchivo)
        self.lA = Label(self, text="Modos de Operación: ", font=('Palatino', 15), bg="#A8DADC", 
                             fg = "#1d3557")
        self.lk = Label(self, text="Llave (8 Caracteres): ", font=('Palatino', 15), bg="#A8DADC", 
                             fg = "#1d3557")
        self.r1 = Radiobutton(self, text="Cipher Code Book",fg="#1d3557",
                              font=('Georgia', 15), bg = "#A8DADC", variable=opcion, value=1)
        self.r2 = Radiobutton(self, text="Cipher Block Chaining",fg="#1d3557",
                              font=('Georgia', 15), bg = "#A8DADC", variable=opcion, value=2)
        self.r3 = Radiobutton(self, text="Cipher Feedback",fg="#1d3557",
                              font=('Georgia', 15), bg = "#A8DADC", variable=opcion, value=3)
        self.r4 = Radiobutton(self, text="Output Feedback",fg="#1d3557",
                              font=('Georgia', 15), bg = "#A8DADC", variable=opcion, value=4)
        self.ek =  Entry(self, width=25)
        
        self.btnCifrar = Button(self, text="Descifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command =lambda: self.Descifrado(opcion.get()), padx=10,pady=15)
       
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
        self.lA.grid(row=2, column = 0, padx=10, pady=15)
        self.lk.grid(row=5, column = 0, padx=10, pady=15, sticky="e" )
        self.r1.grid(row=3, column = 0, padx=10, pady=15)
        self.r2.grid(row=3, column = 1, padx=10, pady=15)
        self.r3.grid(row=4, column = 0, padx=10, pady=15)
        self.r4.grid(row=4, column = 1, padx=10, pady=15)
        self.ek.grid(row=5, column = 1, padx=10, pady=15, sticky="w")
        
        self.btnAbrir.grid(row=1, column = 2, padx=10, pady=15)
        self.btnCifrar.grid(row=6, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=6, column = 0, padx=10, pady=15)
    
    def limpiarDirectorio(self, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
    
    def limpiarNombre(self, cadena):
        it = cadena.index('.bmp')
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[ins+1:it]
    
    def Descifrado(self, op):
        from tkinter import messagebox as MessageBox
        from Cryptodome.Util.Padding import pad, unpad
        llave = self.ek.get()
        if(len(llave)<8):
            for i in range(8-len(llave)):
                llave=llave+'a'
        elif(len(llave)>8):
            llave = llave[0:9]
        
        print(llave)
        
        ext = ""
        op = int(op)
        if(self.dire == 'C:/Users/' or llave== "" ):
            MessageBox.showinfo("Ruta y/o llave no encontradas, ingreselas por favor")
        else:
            llave = bytes(llave, encoding='utf-8')
            ruta= self.limpiarDirectorio(self.dire)    
            nombre = self.limpiarNombre(self.dire)
            image = open(self.dire,"rb")
            
            if(op == 1):
                cifrador = DES.new(llave, DES.MODE_ECB)
                ext = "_descECB"
                nombreDesc = ruta+nombre+ext+".bmp"
                _imDesc = open(nombreDesc,"wb")
                _imDesc.write(image.read(54))
                cifra= image.read()
                
                _imDesc.write(cifrador.decrypt(cifra))
                   
            
                
            elif(op == 2):
                ext = "_descCBC"
                nombreDesc = ruta+nombre+ext+".bmp"
                _imDesc = open(nombreDesc,"wb")
                _file = open(ruta+nombre+"_iv.txt","rb")
                iv = _file.read()
                
                cifrador = DES.new(llave, DES.MODE_CBC, iv)
                _imDesc.write(image.read(54))
                cifra = image.read()
                _imDesc.write(cifrador.decrypt(cifra))
                _file.close()
                
            elif(op == 3):
                
                ext = "_descCFB"
                nombreDesc = ruta+nombre+ext+".bmp"
                _imDesc = open(nombreDesc,"wb")
                _file = open(ruta+nombre+"_iv.txt","rb")
                iv = _file.read()
                
                cifrador = DES.new(llave, DES.MODE_CFB, iv)
                _imDesc.write(image.read(54))
                cifra = image.read()
                _imDesc.write(cifrador.decrypt(cifra))
                _file.close()
            elif(op == 4):
                cifrador = DES.new(llave, DES.MODE_OFB) 
                ext = "_descOFB"
                nombreDesc = ruta+nombre+ext+".bmp"
                _imDesc = open(nombreDesc,"wb")
                _file = open(ruta+nombre+"_iv.txt","rb")
                iv = _file.read()
                
                cifrador = DES.new(llave, DES.MODE_OFB, iv)
                _imDesc.write(image.read(54))
                cifra = image.read()
                _imDesc.write(cifrador.decrypt(cifra))
                _file.close()    
            
            image.close()
            _imDesc.close() 
            
            MessageBox.showinfo("", "Imagen descifrada, encontrarla con la extension "+ext+" en la \n carpeta: "+ruta)
            
           
    
   
    
    def leerArchivo(self):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Seleccione Imagen .bmp",
                                            filetypes =(("bmp files","*.bmp"),
                                                        ("all files", "*.bmp*")))
        self.dire = ruta
