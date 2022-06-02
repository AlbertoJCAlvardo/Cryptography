from tkinter import

def limpiarDirectorio(, cadena):
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[0:ins+1]
    
def limpiarNombre(cadena):
        it = cadena.index('.txt')
        iv = cadena[::-1]
        ins = iv.index('/')
        ins = len(cadena)-(ins+1)       
        return cadena[ins+1:it]
        
    
def leerArchivoTxt():
       
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo txt",
                                            filetypes =(("txt files","*.txt")))
        file = open(ruta, 'r')
        mensaje = file.read()
        file.close()
        return mensaje

def leerArchivoAff():
    
      
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo txt", 
                                               filetypes =(("aff files","*.aff")))
        file = open(ruta, 'r')
        mensaje = file.read()
        file.close()
        return mensaje

def leerArchivoVig():
    
      
        ruta = filedialog.askopenfilename(initialdir = "/", title ="Seleccione Archivo txt", 
                                               filetypes =(("vig files","*.vig")))
        file = open(ruta, 'r')
        mensaje = file.read()
        file.close()
        return mensaje

def escribirArchivoTxt(ruta,nombre, mensaje):
    arNom = open(ruta+nombre+".txt","w")
    arNom.write(mensaje)
    arNom.close()

def escribirArchivoAff(ruta,nombre, mensaje):
    arNom = open(ruta+nombre+".aff","w")
    arNom.write(mensaje)
    arNom.close()
def escribirArchivoVig(ruta,nombre, mensaje):
    arNom = open(ruta+nombre+".Vig","w")
    arNom.write(mensaje)
    arNom.close()

