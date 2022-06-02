from tkinter import*

class Aplicacion(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Programa de Cifrado")
        self.geometry("1200x800")
        self.config(bg="black")
        self.frm = None
        self.switchFrame(Inicial)
        self.mainloop()
        
    def switchFrame(self, n_frame):
        fr = n_frame(self)
        if self.frm is not None:
            self.frm.destroy()
        self.frm = fr
        self.frm.pack()

class Inicial(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg="#5D5958", height="900", width ="650")
        self.ltitulo = Label(self, text="Implementación Criptográfica (Fernet)", font=('', 20, "bold")).grid(row=0, column=1,padx=10, pady=100)
        self.op1 = Button(self, text="  Cifrar  ",
                  font=('', 18, "bold"),        
                  command=lambda: master.switchFrame(frmCifrar)).grid(row=2,column=0, padx=10, pady=15)
        
        self.op2 = Button(self, text="Decifrar", 
                  font=('', 18, "bold"),        
                  command=lambda: master.switchFrame(frmDecifrar)).grid(row=2, column=2, padx=10, pady=15)


class frmCifrar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='gray')
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Cifrar", font=('', 18, "bold"))
        self.lmsj = Label(self, text="Mensaje: ", font=('', 12, "bold"))
        self.btnAbrir = Button(self, text="Abrir Archivo", font=('', 14, "bold"), command = self.leerArchivo)
        self.cMsj = Text(self, width=50, height=10)
        self.btnCifrar = Button(self, text="Cifrar",
                  command = self.Cifrado, padx=10,pady=15)
        self.btnBack = Button(self, text="Volver",
                  command=lambda: master.switchFrame(Inicial),padx = 10) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        self.lmsj.grid(row=2, column = 0, padx=10, pady=15, sticky="nw")
        self.btnAbrir.grid(row=1, column = 1, padx=10, pady=15)
        self.btnCifrar.grid(row=3, column = 2, padx=10, pady=15)
        self.btnBack.grid(row=3, column = 0, padx=10, pady=15)
        self.cMsj.grid(row=2, column = 1, padx=10, pady=15)
        
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
        self.dir = ruta
        file = open(ruta, 'r')
        mensaje = file.read()
        self.cMsj.insert("insert","Mensaje a Cifrar:\n"+mensaje)
        file.close()
        
    
        
    
    def Cifrado(self):
        from cryptography.fernet import Fernet
        
        ruta = self.limpiarDirectorio(self.dir)
        nombre = self.limpiarNombre(self.dir)
        msj = self.cMsj.get("2.0","end-1c")
        clave = Fernet.generate_key()
        cifrador = Fernet(clave)
        msj = msj.replace("\n","%")
        msj = bytes(msj, 'utf-8')
        m_cifrado = cifrador.encrypt(msj)
        clave = str(clave)
        clave = clave[2:len(clave)-1]
        m_cifrado=str(m_cifrado)
        m_cifrado= m_cifrado[2:len(m_cifrado)-1]
        self.cMsj.delete("1.0","end-1c")
        self.cMsj.insert("insert", "Mensaje Cifrado con exito, encontrarlo en la \n carpeta: "+ruta)
        arNom = open(ruta+nombre+"_C.txt","w")
        arNom.write(m_cifrado)
        arNom.close()
        arClav = open(ruta+"Clave de Decifrado.txt", "wb")
        arClav.write(clave)
        arClav.close()





class frmDecifrar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='gray')
        self.dir =  'C:/Users/argen/Desktop/'
        self.ltitulo = Label(self, text="Decifrar", font=('', 18, "bold"))
        self.lmsj = Label(self, text="Mensaje Cifrado: ", font=('', 12, "bold"))
        self.btnAbrir = Button(self, text="Abrir Archivo", font=('', 14, "bold"), command = self.leerArchivo)
        self.cMsj = Text(self, width=50, height=10)
        self.btnDecifrar = Button(self, text="Decifrar",
                  command = self.Decifrado, padx=10,pady=15)
        self.entClave = Entry(self, width = 65)
        self.lblClave = Label(self, text="Clave: ", font=('', 12, "bold"))
        self.btnBack = Button(self, text="Volver",
                  command=lambda: master.switchFrame(Inicial),padx = 10) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        self.lmsj.grid(row=2, column = 0, padx=10, pady=15, sticky="nw")
        self.btnAbrir.grid(row=1, column = 1, padx=10, pady=15)
        self.entClave.grid(row=3, column = 1, padx=10, pady=15, sticky="w")
        self.lblClave.grid(row=3, column = 0, padx=10, pady=15)                    
        self.btnDecifrar.grid(row=4, column = 2, padx=10, pady=15)
        self.btnBack.grid(row= 4, column = 0, padx=10, pady=15)
        self.cMsj.grid(row=2, column = 1, padx=10, pady=15)
    
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
        self.dir = ruta
        file = open(ruta, 'r')
        mensaje = file.read()
        self.cMsj.insert("insert","Mensaje a Decifrar:\n"+mensaje)
        file.close()
    
    def Decifrado(self):
        from cryptography.fernet import Fernet
        
        ruta = self.limpiarDirectorio(self.dir)
        nombre = self.limpiarNombre(self.dir)
        
        m_cifrado = bytes(self.cMsj.get("2.0", "end-1c"), 'utf-8')
        clave = bytes(self.entClave.get(), 'utf-8')
        decifrador = Fernet(clave)
        m_decifrado = str(decifrador.decrypt(m_cifrado))
        m_decifrado = m_decifrado[2:len(m_decifrado)-1]
        m_decifrado = m_decifrado.replace('%',"\n")
        self.cMsj.delete("1.0","end-1c")
        self.cMsj.insert("insert", "Mensaje Decifrado exitosamente, encontrar el archivo en la carpeta:"+ruta)
        arNom = open(ruta+nombre+"_D.txt","w")
        arNom.write(m_decifrado)
        arNom.close()
       
app = Aplicacion()
                    