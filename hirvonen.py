# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:11:29 2022

@author: Ja
"""
import math
import numpy as np

print("METODA HIRVONENA")
x = 3763917
y = 1235727
z = 4982084+15*12
a = 6378137
e2 = 0.00669438002290

def hirvonen(x, y, z, a, e2):
    eps1=0.000001 #sekundy
    eps=eps1/3600*math.pi/180 #rad
    
    #1
    #r=[(x**2+y**2)]**(1/2)
    r=math.sqrt(x**2 + y**2)
    
    #2
    fi=math.atan(z/(r*(1-e2))) #radiany
    fi2=2*fi
    while np.abs(fi2-fi)>eps:
        fi=fi2
        
    #3
        N=a/math.sqrt(1-e2*math.sin(fi2)**2)
        
    #4
        h=(r/np.cos(fi) - N)
        
    #5
        fi2=math.atan(z/(r*(1-e2* (N/(N+h))))) #radiany
        
    #6
    N=a/np.sqrt(1-e2*np.sin(fi2)**2)
    h=r/math.cos(fi) - N
    lam = math.atan(y/x)
    return fi2, lam, h , N

def st_m_s(fi):
    fi=fi*180/math.pi #stopnie
    st=np.floor(fi)
    m=np.floor((fi-st)*60)
    s=((fi-st-m/60)*3600)
    print(st, 'st', m, 'min', round(s, 5), 'sek')

fi, lam, h, N = hirvonen(x, y, z, a, e2)
print(fi, lam, h, N) 
print('fi_A ='), st_m_s(fi)
print('lam_A ='), st_m_s(lam)
print('h_A=', round(h, 3)) 

   
#sprawdzenie
X= (N + h)*np.cos(fi)*np.cos(lam)
print('X_A =', round(X, 11))
Y= (N + h)*np.cos(fi)*np.sin(lam)
print('Y_A =', round(Y, 11))
Z= (N*(1-e2)+h)*np.sin(fi) 
print('Z_A =', round(Z, 11))