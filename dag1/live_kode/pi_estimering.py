# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:11:19 2020

@author: Marie
"""

from pylab import uniform, sqrt


def kast_dart():
    # kast en tilfeldig dart
    # returner koordinatene til kastet
    # x og y skal være mellom -1 og 1
    x_koordinat = uniform(-1, 1)
    y_koordinat = uniform(-1, 1)
    
    return x_koordinat, y_koordinat

def pytagoras(katet1, katet2):
    # Tar inn katetene i en rettvinklet trekant. 
    # returnerer lengden til hypotenus
    return sqrt(katet1**2 + katet2**2)

def traff_blinken(dart_x, dart_y):
    # Tar inn koordinater til dartkast
    # returnere True dersom darten traff
    # False dersom den ikke traff
    avstand_origo = pytagoras(dart_x,
                              dart_y)
    if avstand_origo < 1:
        return True
    else:
        return False

antall_kast = 100000
antall_treff = 0

for kast in range(antall_kast):
    # Kast en dart
    dart_x, dart_y = kast_dart()
    # Sjekk treff
    if traff_blinken(dart_x, dart_y):
        antall_treff += 1
        
estimert_sannsynlighet = antall_treff/antall_kast

estimert_pi = 4*estimert_sannsynlighet

print(f"Antall kast: {antall_kast}")
print(f"Antall treff: {antall_treff}")
print(f"Estimert sannsynlighet: {estimert_sannsynlighet}")
print(f"Estimert pi: {estimert_pi}")


    
    


