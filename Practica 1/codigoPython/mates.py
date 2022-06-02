# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:13:01 2020

@author: argen
"""

def euclides(a, b):
    x = a
    y= b
    while(y>0):
        r = x%y
        x = y
        y = r
    return x

def s_eucExt(a, b):
    if a%b==0:
        return 0
    return int(t_eucExt(b, a%b))

def t_eucExt(a, b):
    if a%b==0:
        return 1
    return int((s_eucExt(b,a%b)- int(a/b)*t_eucExt(b,a%b)))

def eucExt(a, n):
    s = s_eucExt(a,n)
    if s<0:
        return n+s
    return s