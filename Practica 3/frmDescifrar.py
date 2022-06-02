from tkinter import *
from inicial import Inicial

class frmDescifrar(Frame):
    def __init__(self, master):
        import os
        
        self.dire = os.getcwd()
        Frame.__init__(self, master)
        Frame.configure(self,bg="#A8DADC")
        self.ltitulo = Label(self, text="Descifrar", font=('Palatino', 50), bg="#A8DADC", 
                             fg = "#1d3557")
        self.btnAbrir = Button(self, text="Abrir Archivo",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command =lambda: self.leerArchivo(1))
        self.btnOk = Button(self, text="Abrir Llave",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command =lambda: self.leerArchivo(2))
        
        self.btnCifrar = Button(self, text="Descifrar", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8",
                  command =lambda: self.Descifrado(), padx=10,pady=15)
       
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#19535F", fg = "#E8E8E8", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        self.btnDFE = Button(self, text="Descifrar con Firma Electronica",
                               font=('Georgia', 15), bg = "#19535F", fg = "#E8E8E8", command =lambda: self.dfe())
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
       
  
        
        self.btnDFE.grid(row=7, column = 2, padx=10, pady=15)
        self.btnAbrir.grid(row=1, column = 2, padx=10, pady=15)
        self.btnOk.grid(row=1, column = 1, padx=10, pady=15)
        self.btnCifrar.grid(row=6, column = 2, padx=10, pady=10)
        self.btnBack.grid(row=6, column = 0, padx=10, pady=15)
        
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
        
        if(par == 1):
            file = open(ruta, 'rb')
            mensaje = file.read()
            file.close()
            self.msg = mensaje
            self.dire = ruta
        elif(par == 2):
            file = open(ruta, 'r')
            mensaje = file.read()
            file.close()
            self.llave = mensaje
    
    
    def Descifrado(self):
        from tkinter import messagebox as MessageBox
        from Cryptodome.Cipher import PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        import binascii as bi
        
        if(self.llave== "" ):
            MessageBox.showinfo("Ruta y/o llave no encontradas, ingreselas por favor")
        else:
            m = self.msg
            
            ruta = self.limpiarDirectorio(self.dire)
            nombre = self.limpiarNombre(self.dire)
            self.llave =  RSA.importKey(bi.unhexlify(self.llave))
            ct = []
            k = 0
            while k<len(m):
                if(k+256<len(m)):
                    ct.append(m[k:k+256])
                else:
                    ct.append(m[k:len(m)])
                k+=256
            
            
            
            cipher = PKCS1_OAEP.new(self.llave)
            msg = []
            
            for i in ct:
                msg.append(cipher.decrypt(i))
                
            
            
            
            arNom = open(ruta+nombre+"_D.txt","wb")
            for i in msg:
                arNom.write(i)
            arNom.close()
            
    
    def descifrar(self, ct, priv_key):
        from Cryptodome.Cipher import PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        
        cipher = PKCS1_OAEP.new(priv_key)
        msg = []
            
        for i in ct:
            msg.append(cipher.decrypt(i))
                
        plaintext = b"".join(msg)
        return plaintext
    
    def verificar(self, mensaje, public_key, signature):
        from Cryptodome.Hash import SHA1
        from Cryptodome.PublicKey import RSA
        from Cryptodome.Signature import pkcs1_15
        
        h = SHA1.new(mensaje)
        
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return 1;
        except (ValueError, TypeError):
            return 0;
    
    def dfe(self):
            from tkinter import messagebox as MessageBox
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Tu Llave privada",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            file = open(ruta, 'r')
            prkey = file.read()
            file.close()
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="LLave publica del remitente",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            file = open(ruta, 'r')
            pbkey = file.read()
            file.close()
            
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Mensaje a descifrar",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            self.dire = ruta
            file = open(ruta, 'rb')
            mensaje = file.read()
            file.close()
            
            ruta = self.limpiarDirectorio(self.dire)
            nombre = self.limpiarNombre(self.dire)
            
            
            from Cryptodome.PublicKey import RSA
            
            
            import binascii as bi
            pub_key = RSA.importKey(bi.unhexlify(pbkey))
            priv_key = RSA.importKey(bi.unhexlify(prkey))
            
            m = mensaje[256:len(mensaje)]
            signature = mensaje[0:256]
            ct = []
            k = 0
            while k<len(m):
                if(k+256<len(m)):
                    ct.append(m[k:k+256])
                else:
                    ct.append(m[k:len(m)])
                k+=256
                
            plaintext = self.descifrar(ct, priv_key)
            Verificacion = self.verificar(plaintext, pub_key, signature)
            
            
            
            if Verificacion == 1:
                MessageBox.showinfo("","Verificación Correcta")
                arNom = open(ruta+nombre+"_DFirma Digital.txt","wb")  
                arNom.write(plaintext)
                arNom.close()
            else:
                MessageBox.showinfo("","Fallo en la Verificación")
            
            
            arNom = open(ruta+nombre+"_DFirma Digital.txt","wb")  
            arNom.write(plaintext)
            arNom.close()