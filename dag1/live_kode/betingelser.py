# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:19:53 2020

@author: Marie
"""

"""
dette 
er 
en 
lang 
kommentar
"""

temperatur = float(input("Hva er temperaturen? "))

frysepunkt = 0 #C
kokepunkt = 100 #C

if temperatur < frysepunkt:
    print("Det er et fast stoff")
elif temperatur < kokepunkt:
    print("Det er en væske")
else:
    print("Det er en gass")
    
    