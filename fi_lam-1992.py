# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:21:35 2022

@author: Ja
"""
import math
import numpy as np

print('UKŁAD 1992')

#HIRVONEN
fi_A = 0.9022977821385849
lam_A = 0.3172216610312846
#KIVIOJ
fi_B = 0.9030457997127278
lam_B = 0.32601059537730337

a = 6378137
e2 = 0.00669438002290
e_2 = e2 / (1-e2)
#skala pld srodkowego
m_0 = 0.9993 #odwzorowanie poludnika srodkowa na linie prosta w skali : 0.9993

def uklad_1992(fi, lam, a, e2, m_0):
    N = a/(math.sqrt(1-e2 * np.sin(fi)**2))
    t = np.tan(fi)
    n2 = e_2 * np.cos(lam)**2
    lam_0 = math.radians(19) #poczatek ukladu w punkcie przeciecia poludnika L0 = 19st z obrazem równika 
    l = lam - lam_0
    
    A_0 = 1 - (e2/4) - (3*(e2**2))/64 - (5*(e2**3))/256
    A_2 = 3/8 * (e2 + ((e2**2)/4) + ((15*e2**3)/128))
    A_4 = 15/256 * (e2**2 + (3*(e2**3))/4)
    A_6 = (35*(e2**3))/3072
    
    sigma = a* ((A_0*fi) - (A_2*np.sin(2*fi)) + (A_4*np.sin(4*fi)) - (A_6*np.sin(6*fi)))
    
    x = sigma + ((l**2)/2) * (N*np.sin(fi)*np.cos(fi)) * (1 + ((l**2)/12) * ((np.cos(fi))**2) * (5 - t**2 + 9*n2 + (4*n2**2)) + ((l**4)/360) * ((np.cos(fi))**4) * (61 - (58*(t**2)) + (t**4) + (270*n2) - (330 * n2 *(t**2))))
    y = l * (N*np.cos(fi)) * (1 + ((((l**2)/6) * (np.cos(fi))**2) * (1-(t**2) + n2)) +  (((l**4)/(120)) * (np.cos(fi)**4)) * (5 - (18 * (t**2)) + (t**4) + (14*n2) - (58*n2*(t**2))))

    x92 = round(x * m_0 - 5300000, 3)
    y92 = round(y * m_0 + 500000, 3)   
    
    return x92, y92 

x, y = uklad_1992(fi_A, lam_A, a, e2, m_0)
x1, y1 = uklad_1992(fi_B, lam_B, a, e2, m_0)

print('wspolrzedne punktu poczatkowego:')
print('x_92A =', x)
print('y_92A =', y)
print('wspolrzedne punktu koncowego:')
print('x_92B =', x1)
print('y_92B =', y1)