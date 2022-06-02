
def cifVig(mensaje, clave):
    mensaje = list(mensaje)
    clave = list(clave)
    cif = []
    for i in range(len(mensaje)):
        p = ord(mensaje[i])
        k = ord(clave[i%len(clave)])
        c = (p + k) % 256
        cif.append(chr(c))
    cif = "".join(cif)
    return cif

def decifVig(mcif, clave):
    mcif = list(mcif)
    clave = list(clave)
    mensaje = []
    for i in range(len(mcif)):
        c = ord(mcif[i])
        invK = 256 - ord(clave[i%len(clave)])
        p = (c+ invK)%256;
        mensaje.append(chr(p))
    mensaje = "".join(mensaje)
    return mensaje
