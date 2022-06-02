from PIL import Image
import binascii
import os
import io

with open("thundercats.bmp", "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)
    


header = b[1:60]
c = b[433:len(b)]    

for i in range(55,len(b)):
    c[i-433] = (b[i]+20)%256
t = bytes(header)+bytes(c)    
chorizo = bytearray()
chorizo[0:] = b[0:]
chorizo = bytes(chorizo) 

image = Image.open(io.BytesIO(chorizo))
image.save("otra.bmp", 'bmp') 