# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:56:56 2021

@author: argen
"""

from tkinter import filedialog
import os

dire = os.getcwd()       

ruta = filedialog.askopenfilename(initialdir = dire, title ="Modo Texto",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
        
file = open(ruta, 'rb')
mensaje = file.read()
file.close()

ruta = filedialog.askopenfilename(initialdir = dire, title ="Llave pública",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
        
file = open(ruta, 'r')
llave = file.read()
file.close()

from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
import binascii as bi



llave =  RSA.importKey(bi.unhexlify(llave))
k=0
pt = []
i = 0
while i<len(mensaje):
    if(i+128<len(mensaje)):
        pt.append(mensaje[i:i+128])
    else:
        pt.append(mensaje[i:len(mensaje)])
    i+=128

c = []

for i in pt:              
    cipher = PKCS1_OAEP.new(llave)
    c.append(cipher.encrypt(i))

ruta = filedialog.askopenfilename(initialdir = dire, title ="Llave privada",
                                            filetypes =(("txt files","*.txt"),
                                                        ("all files", "*.*")))
file = open(ruta, 'r')
prk = file.read()
file.close()
prk = RSA.importKey(bi.unhexlify(prk))
msg = []
cipher = PKCS1_OAEP.new(prk)
i=0
for i in c:
            msg.append(cipher.decrypt(i))
            
