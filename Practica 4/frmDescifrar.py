from tkinter import *
from inicial import Inicial

class frmDescifrar(Frame):
    def __init__(self, master):
        import os
        
        self.dire = os.getcwd()
        Frame.__init__(self, master)
        Frame.configure(self,bg="#000000")
        self.ltitulo = Label(self, text="Descifrar", font=('Palatino', 50), bg="#000000", 
                             fg = "#ffffff")
       
        
        self.btnCifrar = Button(self, text="Descifrar", font=('Georgina', 15), bg = "#000000", fg = "#ffffff",
                  command =lambda: self.Descifrado(), padx=10,pady=15)
       
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#000000", fg = "#ffffff", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        self.btnDFE = Button(self, text="Descifrar con Firma Electronica",
                               font=('Georgia', 15), bg = "#000000", fg = "#ffffff", command =lambda: self.dfe())
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
       
  
        
        self.btnDFE.grid(row=7, column = 2, padx=10, pady=15)
       
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
    def descifrar(self, ciphertext, priv_key):
        from Cryptodome.Cipher import PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        from Cryptodome.Cipher import AES
        
        cipher_rsa = PKCS1_OAEP.new(priv_key)
        session_key = cipher_rsa.decrypt(ciphertext[0:256])
        cipher_aes = AES.new(session_key, AES.MODE_ECB)
        
        plaintext = cipher_aes.decrypt(ciphertext[256:len(ciphertext)])
            
       
        return plaintext
    
    def Descifrado(self):
        from tkinter import filedialog
        from tkinter import messagebox as MessageBox
        from Cryptodome.Cipher import PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        import binascii as bi
        
        if(1):
            
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Tu Llave privada",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            file = open(ruta, 'r')
            prkey = file.read()
            file.close()
            
            
            ruta = filedialog.askopenfilename(initialdir = self.dire, title ="Mensaje a descifrar",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
            self.dire = ruta
            file = open(ruta, 'rb')
            mensaje = file.read()
            file.close()
            
            m = self.msg
            nombre = self.limpiarNombre(ruta)
            ruta = self.limpiarDirectorio(ruta)
            
            self.llave =  RSA.importKey(bi.unhexlify(prkey))
            
            
            plaintext = self.descifrar(mensaje, self.llave)
            
           
            
            
            
            arNom = open(ruta+nombre+"_D.txt","wb")
            arNom.write(plaintext)
            arNom.close()
            
    
    
    
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
            
            signature = mensaje[0:256]
            llave_cifra = mensaje[256:len(mensaje)]
                
            plaintext = self.descifrar(llave_cifra, priv_key)
            Verificacion = self.verificar(plaintext, pub_key, signature)
            
            
            
            if Verificacion == 1:
                MessageBox.showinfo("","Verificación Correcta")
               
            else:
                MessageBox.showinfo("","Fallo en la Verificación")
            
            
            arNom = open(ruta+nombre+"_DFirma Digital.txt","wb")  
            arNom.write(plaintext)
            arNom.close()