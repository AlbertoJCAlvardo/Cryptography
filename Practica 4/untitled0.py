# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:14:44 2021

@author: argen
"""

def binario(n):
    resultado = []
    for i in range(8):
        resultado.append(n & 1)
        n >>= 1
    for i in range(len(resultado)):
        resultado[i] = str(resultado[i])
    return resultado


for i in range(256):
    l = binario(i)
    l = l[::-1]
    k = "".join(l)
    print(k,"\n")