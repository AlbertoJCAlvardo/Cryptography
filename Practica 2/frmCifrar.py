from tkinter import *
from inicial import Inicial
from Cryptodome.Cipher import DES

class frmCifrar(Frame):
    def __init__(self, master):
        import os
        opcion = IntVar()
        
        self.dire = os.getcwd()
        Frame.__init__(self, master)
        Frame.configure(self,bg="#A8DADC")
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Cifrar", font=('Palatino', 50), bg="#A8DADC", 
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
        
        self.btnCifrar = Button(self, text="Cifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command =lambda: self.Cifrado(opcion.get()), padx=10,pady=15)
       
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
    
    def Cifrado(self, op):
        from tkinter import messagebox as MessageBox
        from Cryptodome.Util.Padding import pad, unpad
        llave = self.ek.get()
        if(len(llave)<8):
            for i in range(8-len(llave)):
                llave=llave+'a'
        elif(len(llave)>8):
            llave = llave[0:8]
        
        
        ext = ""
        op = int(op)
        if(self.dire == 'C:/Users/' or llave== "" ):
            MessageBox.showinfo("Ruta y/o llave no encontradas, ingreselas por favor")
        else:
            ruta= self.limpiarDirectorio(self.dire)    
            nombre = self.limpiarNombre(self.dire)
            image = open(self.dire,"rb")
            
            llave = bytes(llave, encoding='utf-8')
            if(op == 1):
                cifrador = DES.new(llave, DES.MODE_ECB)
                ext = "_cifECB"
                nombreCifra = ruta+nombre+ext+".bmp"
                _image = open(nombreCifra,"wb")
                _file = open(ruta+nombre+ext+"_iv.txt","wb")
                _image.write(image.read(54))
                plaintext= image.read()
                
                _image.write(cifrador.encrypt(plaintext))
            
                
            elif(op == 2):
                cifrador = DES.new(llave, DES.MODE_CBC)
                ext = "_cifCBC"
                nombreCifra = ruta+nombre+ext+".bmp"
                _image = open(nombreCifra,"wb")
                _file = open(ruta+nombre+ext+"_iv.txt","wb")
                _image.write(image.read(54))
                plaintext= image.read()
                _file.write(cifrador.iv)
                _image.write(cifrador.encrypt(plaintext))

                
            elif(op == 3):
                cifrador = DES.new(llave, DES.MODE_CFB)
                ext = "_cifCFB"
                nombreCifra = ruta+nombre+ext+".bmp"
                _image = open(nombreCifra,"wb")
                _file = open(ruta+nombre+ext+"_iv.txt","wb")
                _image.write(image.read(54))
                plaintext= image.read()
                _file.write(cifrador.iv)
                _image.write(cifrador.encrypt(plaintext))
                
            elif(op == 4):
                cifrador = DES.new(llave, DES.MODE_OFB) 
                ext = "_cifOFB"
                nombreCifra = ruta+nombre+ext+".bmp"
                _image = open(nombreCifra,"wb")
                _file = open(ruta+nombre+ext+"_iv.txt","wb")
                _image.write(image.read(54))
                plaintext= image.read()
                _file.write(cifrador.iv)
                _image.write(cifrador.encrypt(plaintext))
            
            _file.close()
            image.close()
            _image.close()
            
            
            
            
            MessageBox.showinfo("", "Imagen cifrada, encontrarla con la extension "+ext+" en la \n carpeta: "+ruta)
           
           
    
   
    
    def leerArchivo(self):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Seleccione Imagen .bmp",
                                            filetypes =(("bmp files","*.bmp"),
                                                        ("all files", "*.bmp*")))
        self.dire = ruta
