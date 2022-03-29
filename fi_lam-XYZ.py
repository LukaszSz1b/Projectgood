# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:51:56 2022

@author: Ja
"""
import math as m
import numpy as np

e2 = 0.00669438002290
a = 6378137


fia = 52 * np.pi / 180
lamaa = 20.5 * np.pi / 180
Ha = 100    
    
#dane satelity:
fis = 0 * np.pi / 180
lams = 4 * np.pi / 180
Hs = 35794170


Na = a / np.sqrt(1 - e2 * np.sin(fia)**2)
print('Na = ', Na)
Ma = (a * (1 - e2)) / (m.sqrt(1 - e2 * (np.sin(fia))**2)**3)

Xa = (Na + Ha)*np.cos(fia)*np.cos(lamaa)
print('X_A =', round(Xa, 11))
Ya = (Na + Ha)*np.cos(fia)*np.sin(lamaa)
print('Y_A =', round(Ya, 11))
Za = (Na * (1 - e2) + Ha) * np.sin(fia) 
print('Z_A =', round(Za, 11))