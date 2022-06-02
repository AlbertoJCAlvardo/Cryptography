# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:41:19 2020

@author: argen
"""

from Affine import *
c = cifAffine("Hola mundo",1,11,97)
d = decifAffine(c,1,11,97)

print(c,"\n",d)