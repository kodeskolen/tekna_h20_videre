# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:09:14 2020

@author: Marie
"""

from pylab import pi

def grader_til_radianer(grader):
    # Tar inn en vinkel i grader
    # returnerer vinkelen i radianer
    return pi*grader/180

vinkel = 90
vinkel_radianer = grader_til_radianer(vinkel)
print(vinkel_radianer)