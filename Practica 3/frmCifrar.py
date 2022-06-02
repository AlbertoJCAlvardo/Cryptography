from tkinter import *
from inicial import Inicial

class frmCifrar(Frame):
    def __init__(self, master):
        import os
        
        self.dire = os.getcwd()
        Frame.__init__(self, master)
        Frame.configure(self,bg="#A8DADC")
        self.ltitulo = Label(self, text="Cifrar", font=('Palatino', 50), bg="#A8DADC", 
                             fg = "#1d3557")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command =lambda: self.leerArchivo(1))
        self.btnOk = Button(self, text="Abrir Llave",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command =lambda: self.leerArchivo(2))
        
        self.btnCFE = Button(self, text="Cifrar con Firma Electronica",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command =lambda: self.cfe())
        
        self.btnCifrar = Button(self, text="Cifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command =lambda: self.Cifrado(), padx=10,pady=15)
       
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
       
  
        
        
        self.btnAbrir.grid(row=1, column = 2, padx=10, pady=15)
        self.btnOk.grid(row=1, column = 1, padx=10, pady=15)
        self.btnCifrar.grid(row=6, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=6, column = 0, padx=10, pady=15)
        self.btnCFE.grid(row=7,column=2,padx=10,pady=15)
        
        self.msg = ""
        self.llave = ""
    
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
        
    
    def leerArchivo(self, par):
        from tkinter import filedialog
       
        ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Seleccione Archivo txt",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
        
        file = open(ruta, 'r')
        mensaje = file.read()
        file.close()
        if(par == 1):
            self.msg = mensaje
            self.dire = ruta
        elif(par == 2):
            self.llave = mensaje
    
    
    def Cifrado(self):
        from tkinter import messagebox as MessageBox
        from Cryptodome.Cipher import PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        import binascii as bi
        
        if(self.llave== "" ):
            MessageBox.showinfo("Ruta y/o llave no encontradas, ingreselas por favor")
        else:
            m = self.msg
            m = m.encode()
            pt = []
            k=0
            while k<len(m):
                if(k+128<len(m)):
                    pt.append(m[k:k+128])
                else:
                    pt.append(m[k:len(m)])
                k+=128
            
            ruta = self.limpiarDirectorio(self.dire)
            nombre = self.limpiarNombre(self.dire)
            self.llave =  RSA.importKey(bi.unhexlify(self.llave))
            
            c=[]
            cipher = PKCS1_OAEP.new(self.llave)
            
            for i in pt:            
                c.append(cipher.encrypt(i))
                
            
            
            arNom = open(ruta+nombre+"_C.txt","wb")
            for i in c:    
                arNom.write(i)
            arNom.close()
    def cifrar(self, ptlist, pub_key):
                from tkinter import messagebox as MessageBox
                from Cryptodome.Cipher import PKCS1_OAEP
                from Cryptodome.PublicKey import RSA
                ctlist=[]
                cipher = PKCS1_OAEP.new(pub_key)
                for i in ptlist:            
                    ctlist.append(cipher.encrypt(i))
                return ctlist
                
                
    def firmar(self, plaintext, priv_key):
                from Cryptodome.Signature import pkcs1_15
                from Cryptodome.Hash import SHA1
                from Cryptodome.PublicKey import RSA
                
                h = SHA1.new(plaintext)
                signature = pkcs1_15.new(priv_key).sign(h)
                
                return signature
        
    def cfe(self):
            from tkinter import filedialog
            from tkinter import messagebox as MessageBox
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Tu Llave privada",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            file = open(ruta, 'r')
            prkey = file.read()
            file.close()
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="LLave publica del destinatario",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            file = open(ruta, 'r')
            pbkey = file.read()
            file.close()
            
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Mensaje a cifrar",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            file = open(ruta, 'rb')
            mensaje = file.read()
            file.close()
            
            

            
            
            self.dire = ruta
            ruta = self.limpiarDirectorio(self.dire)
            nombre = self.limpiarNombre(self.dire)
            from Cryptodome.PublicKey import RSA
            
            import binascii as bi
            pub_key = RSA.importKey(bi.unhexlify(pbkey))
            priv_key = RSA.importKey(bi.unhexlify(prkey))
            
            m = mensaje
            ptlist = []
            k=0
            while k<len(m):
                if(k+128<len(m)):
                    ptlist.append(m[k:k+128])
                else:
                    ptlist.append(m[k:len(m)])
                k+=128
            
            ctlist = self.cifrar(ptlist, pub_key)
            signature = self.firmar(m, priv_key)
            
            
            
            
            MessageBox.showinfo("","Archivo Cifrado con Firma digital")
            arNom = open(ruta+nombre+"_CFirmaDigital.txt","wb")  
            arNom.write(signature)
            for i in ctlist:
                arNom.write(i)
            arNom.close()
            
            print("sig:",len(signature),"brick:",len(ctlist[0]))
            
            
            
            
                    
                
           
    
   
    

