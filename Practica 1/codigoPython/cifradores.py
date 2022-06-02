from tkinter import *
from inicial import *
from Affine import *
from Vigenere import *
from tkinter import messagebox as MessageBox

class frmAffine(Frame):
     def __init__(self, master):
        Frame.__init__(self, master)
        opcion = IntVar()
        self.config(bg="#564256", height="600", width ="800")
        self.ltitulo = Label(self, text="Affine\nMenú", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8").grid(row=0, column=1,padx=100, pady=50)
        self.op1 = Button(self, text="  Cifrar  ", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",       
                  command=lambda: master.switchFrame(frmCifAffine)).grid(row=2,column=0, padx=10, pady=15)
        
        self.op2 = Button(self, text="Descifrar",  font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",        

                         command=lambda: master.switchFrame(frmDecifAffine)).grid(row=2, column=2, padx=10, pady=15)

class frmVig(Frame):
     def __init__(self, master):
        Frame.__init__(self, master)
        opcion = IntVar()
        self.config(bg="#457b9d", height="600", width ="800")
        self.ltitulo = Label(self, text="Vigenère\nMenú", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8").grid(row=0, column=1,padx=100, pady=50)
        self.op1 = Button(self, text="  Cifrar  ", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",       
                  command=lambda: master.switchFrame(frmCifVig)).grid(row=2,column=0, padx=10, pady=15)
        
        self.op2 = Button(self, text="Descifrar",  font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",        

                         command=lambda: master.switchFrame(frmDecifVig)).grid(row=2, column=2, padx=10, pady=15)

class frmCifAffine(Frame):
    def __init__(self, master):
        
        n = IntVar()
        al = IntVar()
        be = IntVar()
        dire = 'C:/Users/argen/Desktop/'
        Frame.__init__(self, master)
        Frame.configure(self,bg="#564256")
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Cifrar", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", command = self.leerArchivo)
        self.lN = Label(self, text="Numero de Caracteres en el afabeto: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        self.lA = Label(self, text="Alfa: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        self.lB = Label(self, text="Beta: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        self.cA = Label(self, text="Conjunto Alfa ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        self.tAl = Text(self, width=20, height =4)
        self.eN =  Entry(self, width=10)
        self.eB =  Entry(self, width=10)
        self.eA =  Entry(self, width=10)
        
        self.btnCifrar = Button(self, text="Cifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command = self.Cifrado, padx=10,pady=15)
        self.btnOk = Button(self, text="Ok", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command = self.printAlfa, padx=10,pady=15)
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(frmAffine),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        self.lN.grid(row=2, column = 1, padx=10, pady=15)
        self.lA.grid(row=4, column = 0, padx=10, pady=15)
        self.cA.grid(row =3, column = 0, padx=10, pady=15)
        self.lB.grid(row=4, column = 2, padx=10, pady=15)
        
        self.eN.grid(row=2, column =2, padx=10, pady=15, sticky="w")
        self.tAl.grid(row=3, column=1, padx=20, pady=4)
        self.eA.grid(row=4, column =1, padx=10, pady=15, sticky="nw")
        self.eB.grid(row=4, column =3, padx=10, pady=15, sticky="nw")
        
        self.btnOk.grid(row=2, column=3,  padx=10, pady=15)
        self.btnAbrir.grid(row=1, column = 1, padx=10, pady=15)
        self.btnCifrar.grid(row=5, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=5, column = 0, padx=10, pady=15)
       
    def printAlfa(self):
        self.n = int(self.eN.get())
        conj = conAlfa(self.n)
        cad = "{"
        for i in range(len(conj)):
            cad = cad+str(conj[i])
            if i!=len(conj)-1:
                cad = cad+", "
        self.tAl.insert("insert",cad)
            
    def limpiarDirectorio(self, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
    
    def limpiarNombre(self, cadena):
        it = cadena.index('.txt')
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[ins+1:it]
        
    
    def leerArchivo(self):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo txt",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
        self.dire = ruta
        
    def obtenerMensaje(self):
        file = open(self.dire, 'rt')
        mensaje = file.read()
        file.close()
        return str(mensaje)
    
    def Cifrado(self):
        n = self.n
        ruta = self.limpiarDirectorio(self.dire)
        nombre = self.limpiarNombre(self.dire)
        mensaje = self.obtenerMensaje()
        
        if len(self.eA.get()) == 0:
            self.al = generarAlfa(n)
        else:
            self.al = int(self.eA.get())
        if len(self.eB.get()) == 0:
            self.be = generarBeta(n)
        else:
            self.be = int(self.eB.get())
        
        if validarAlfa(self.al, n)  and validarBeta(self.be, n):
            self.eA.delete(0, 'end')
            self.eA.insert("insert",str(self.al))
            self.eB.delete(0, 'end')
            self.eB.insert("insert",str(self.be))
            MessageBox.showinfo("", "Mensaje Cifrado con exito, encontrarlo con la extension .aff en la \n carpeta: "+ruta)
            
            m_cifrado = cifAffine(mensaje, self.al, self.be, n)
            arNom = open(ruta+nombre+".aff","w", encoding = "utf-8")
            arNom.write(m_cifrado)
            arNom.close()
            llaves = "Alfa: "+str(self.al)+" Beta: "+str(self.be)
            arClav = open(ruta+"Clave de Decifrado "+nombre+".txt", "wt")
            arClav.write(llaves)
            arClav.close()
        else:
            MessageBox.showinfo("Error", "Alfa y/o Beta incorrectos, intentelo de nuevo.")
            self.eA.delete(0, 'end')
            self.eB.delete(0, 'end')
    
class frmDecifAffine(Frame):
    def __init__(self, master):
        
        n = IntVar()
        al = IntVar()
        be = IntVar()
        dire = 'C:/Users/argen/Desktop/'
        Frame.__init__(self, master)
        Frame.configure(self,bg="#564256")
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Decifrar Affine", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", command = self.leerArchivo)
        self.lN = Label(self, text="Numero de Caracteres en el afabeto: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        self.lA = Label(self, text="Alfa: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        self.lB = Label(self, text="Beta: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        
        self.eN =  Entry(self, width=10)
        self.eB =  Entry(self, width=10)
        self.eA =  Entry(self, width=10)
        
        self.btnDecifrar = Button(self, text="Decifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command = self.Decifrado, padx=10,pady=15)
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        self.lN.grid(row=2, column = 1, padx=10, pady=15)
        self.lA.grid(row=4, column = 0, padx=10, pady=15)
        self.lB.grid(row=4, column = 2, padx=10, pady=15)
        
        self.eN.grid(row=2, column =2, padx=10, pady=15, sticky="w")
        self.eA.grid(row=4, column =1, padx=10, pady=15, sticky="nw")
        self.eB.grid(row=4, column =3, padx=10, pady=15, sticky="nw")
        
        self.btnAbrir.grid(row=1, column = 1, padx=10, pady=15)
        self.btnDecifrar.grid(row=5, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=5, column = 0, padx=10, pady=15)
       
  
            
    def limpiarDirectorio(self, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
    
    def limpiarNombre(self, cadena):
        it = cadena.index('.aff')
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[ins+1:it]
        
    
    def leerArchivo(self):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo .aff",
                                            filetypes =(("txt files","*.aff"),
                                                        ("all files", "*.*")))
        self.dire = ruta
        
    def obtenerMensaje(self):
        file = open(self.dire, 'rt', encoding="utf-8")
        mensaje = file.read()
        file.close()
        return mensaje
    
    def Decifrado(self):
        self.n = int(self.eN.get())
        n = self.n
        ruta = self.limpiarDirectorio(self.dire)
        nombre = self.limpiarNombre(self.dire)
        mcifrado = self.obtenerMensaje()
        
        if len(self.eA.get()) == 0:
            self.al = n
        else:    
            self.al = int(self.eA.get())
        if len(self.eB.get()) == 0:
            self.be = 0
        else:
            self.be = int(self.eB.get())
            
        MessageBox.showinfo("", "Mensaje Decifrado, encontrarlo con la extension .txt en la \n carpeta: "+ruta)
        msg = decifAffine(mcifrado, self.al, self.be, n)
        arNom = open(ruta+nombre+"_D.txt","w", encoding="utf-8")
        arNom.write(msg)
        arNom.close()
            
class frmCifVig(Frame):
    def __init__(self, master):
        
        n = IntVar()
        al = IntVar()
        be = IntVar()
        dire = 'C:/Users/argen/Desktop/'
        Frame.__init__(self, master)
        Frame.configure(self,bg="#564256")
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Cifrar Vigènere", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", command = self.leerArchivo)
        
        self.clave = Label(self, text="Clave: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        
       
     
        self.eclave =  Entry(self, width=10)
        
        
        self.btnCifrar = Button(self, text="Cifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command = self.Cifrado, padx=10,pady=15)
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
        self.clave.grid(row=3, column = 0, padx=10, pady=15)
        
        
        
        self.eclave.grid(row=3, column=1, padx=20, pady=4)
        
        self.btnAbrir.grid(row=1, column = 1, padx=10, pady=15)
        self.btnCifrar.grid(row=5, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=5, column = 0, padx=10, pady=15)
       
            
    def limpiarDirectorio(self, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
    
    def limpiarNombre(self, cadena):
        it = cadena.index('.txt')
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[ins+1:it]
        
    
    def leerArchivo(self):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo txt",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
        self.dire = ruta
        
    def obtenerMensaje(self):
        file = open(self.dire, 'rt')
        mensaje = file.read()
        file.close()
        return str(mensaje)
    
    def Cifrado(self):
        
       if len(self.eclave.get())==0:
           MessageBox.showinfo("", "Introduzca los valores que se le piden")
       else:
          
           self.clave = self.eclave.get()
           clave = self.clave
           ruta = self.limpiarDirectorio(self.dire)
           nombre = self.limpiarNombre(self.dire)
           mensaje = self.obtenerMensaje()
           m_cifrado = cifVig(mensaje, clave)
           arNom = open(ruta+nombre+".vig","w", encoding = "utf-8")
           arNom.write(m_cifrado)
           arNom.close()
           arClav = open(ruta+"Clave de Decifrado "+nombre+".txt", "wt")
           arClav.write(clave)
           arClav.close()
           MessageBox.showinfo("", "Mensaje Cifrado exitosamente, encontrar con la extension .vig sen la ruta: "+ruta)
        
           
class frmDecifVig(Frame):
    def __init__(self, master):
        
        n = IntVar()
        al = IntVar()
        be = IntVar()
        dire = 'C:/Users/argen/Desktop/'
        Frame.__init__(self, master)
        Frame.configure(self,bg="#564256")
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Decifrar Vigènere", font=('Chiller', 50), bg="#564256", 
                             fg = "#E8E8E8")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", command = self.leerArchivo)
        
        self.clave = Label(self, text="Clave: ", font=('Chiller', 15), bg="#564256", 
                             fg = "#E8E8E8")
        
       
     
        self.eclave =  Entry(self, width=10)
        
        
        self.btnCifrar = Button(self, text="Decifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command = self.Cifrado, padx=10,pady=15)
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
        self.clave.grid(row=3, column = 0, padx=10, pady=15)
        
        
        
        self.eclave.grid(row=3, column=1, padx=20, pady=4)
        
        self.btnAbrir.grid(row=1, column = 1, padx=10, pady=15)
        self.btnCifrar.grid(row=5, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=5, column = 0, padx=10, pady=15)
       
            
    def limpiarDirectorio(self, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
    
    def limpiarNombre(self, cadena):
        it = cadena.index('.vig')
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[ins+1:it]
        
    
    def leerArchivo(self):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo vig",
                                            filetypes =(("vig files","*.vig"),
                                                        ("all files", "*.*")))
        self.dire = ruta
        
    def obtenerMensaje(self):
        file = open(self.dire, 'rt', encoding="utf-8", errors="ignore")
        mensaje = file.read()
        file.close()
        return str(mensaje)
    
    def Cifrado(self):
        
       if  len(self.eclave.get())==0:
           MessageBox.showinfo("", "Introduzca los valores que se le piden")
       else:
          
           self.clave = self.eclave.get()
           clave = self.clave
           ruta = self.limpiarDirectorio(self.dire)
           nombre = self.limpiarNombre(self.dire)
           m_cifrado = self.obtenerMensaje()
           mensaje = decifVig(m_cifrado, clave)
           
           arNom = open(ruta+nombre+"_D.txt","w", encoding = "utf-8")
           arNom.write(mensaje)
           arNom.close()
           MessageBox.showinfo("", "Mensaje decirfrado, encontrar en la ruta: "+ruta)
        
           


