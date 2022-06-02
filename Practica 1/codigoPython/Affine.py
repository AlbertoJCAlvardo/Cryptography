# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:41:51 2020

@author: argen
"""
from random import randint

from mates import *
def validarAlfa(b, n):
    if euclides(b,n) == 1:
        return True
    return False
    
def validarBeta(b, n):
    if 0<b<n:
        return True
    return False
def generarAlfa(n):
    alfa = []
    for i in range(n):
        if euclides(i, n) == 1:
            alfa.append(i)
    return alfa[randint(0, len(alfa))-1]

def generarBeta(n):
    return randint(0, n)

def conAlfa(n):
    alfa = []
    for i in range(n):
        if euclides(i, n) == 1:
            alfa.append(i)
      
    return alfa
    
def cifAffine(mensaje, alfa, beta, n):
    mensaje = list(mensaje)
    mcifrado = []
    for i in range(len(mensaje)):
        p = ord(mensaje[i])%n
        c = (alfa*p + beta)%n
        mcifrado.append(chr(c))
        
    mcifrado = "".join(mcifrado)
    return mcifrado;

def decifAffine(cif, alfa, beta, n):
    cif = list(cif)
    invA = eucExt(alfa,n)
    invB = n-beta
    invB = invA*invB
    mensaje = []
    for i in range(len(cif)):
        c = ord(cif[i])
        p = (invA*c + invB)% n
        mensaje.append(chr(p))
    mensaje = "".join(mensaje)
    return mensaje
        
        
    