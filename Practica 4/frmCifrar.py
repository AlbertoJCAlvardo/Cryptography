from tkinter import *
from inicial import Inicial

class frmCifrar(Frame):
    def __init__(self, master):
        import os
        
        self.dire = os.getcwd()
        Frame.__init__(self, master)
        Frame.configure(self,bg="#000000")
        self.ltitulo = Label(self, text="Cifrar", font=('Palatino', 50), bg="#000000", 
                             fg = "#ffffff")
       
        
        self.btnCFE = Button(self, text="Cifrar con Firma Electronica",
                               font=('Georgia', 15), bg = "#000000", fg = "#ffffff", command =lambda: self.cfe())
        
        self.btnCifrar = Button(self, text="Cifrar", font=('Georgina', 15), bg = "#000000", fg = "#ffffff",
                  command =lambda: self.Cifrado(), padx=10,pady=15)
       
        self.btnBack = Button(self, text="Volver", font=('Georgina', 15), bg = "#000000", fg = "#ffffff", 
                  command=lambda: master.switchFrame(Inicial),padx = 15) 
        
        self.ltitulo.grid(row=0, column = 1, padx=10, pady=15)
        
        
       
  
        
        
        
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
    def cifrar(self, plaintext, pub_key):
                from tkinter import messagebox as MessageBox
                from Cryptodome.Cipher import PKCS1_OAEP
                from Cryptodome.Cipher import AES
                from Cryptodome.PublicKey import RSA
                from Cryptodome.Random import get_random_bytes 
                
                session_key = get_random_bytes(16)
                cipher_rsa = PKCS1_OAEP.new(pub_key)
                cipher_aes = AES.new(session_key, AES.MODE_ECB)
                
                    
                enc_aes_key = cipher_rsa.encrypt(session_key)
                ciphertext = cipher_aes.encrypt(plaintext)
                
                print(len(enc_aes_key))
                
                chorizo = enc_aes_key + ciphertext
                return chorizo
    
    def Cifrado(self):
        from tkinter import filedialog
        from tkinter import messagebox as MessageBox
        from Cryptodome.Cipher import PKCS1_OAEP
        from Cryptodome.PublicKey import RSA
        import binascii as bi
        
        if(1):
            
           
            
            
            
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
            
            
            nombre = self.limpiarNombre(ruta)
            ruta = self.limpiarDirectorio(ruta)
            
            self.llave =  RSA.importKey(bi.unhexlify(pbkey))
            
            llave_cifra = self.cifrar(mensaje, self.llave)
                
            
            
            arNom = open(ruta+nombre+"_C.txt","wb")
            
            arNom.write(llave_cifra)
            arNom.close()
   
                
                
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
           
            
            
            llave_cifra = self.cifrar(m, pub_key)
            signature = self.firmar(m, priv_key)
            
            
            
            
            MessageBox.showinfo("","Archivo Cifrado con Firma digital")
            arNom = open(ruta+nombre+"_CFirmaDigital.txt","wb")  
            arNom.write(signature)
            
            arNom.write(llave_cifra)
            arNom.close()
            
            
            
            
            
            
                    
                
           
    
   
    

