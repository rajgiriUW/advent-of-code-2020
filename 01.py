# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:03:23 2020

@author: Raj
"""


import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
data = np.sort(np.loadtxt(base + r'/01_nums.txt'))

for  x  in data:

    if 2020 - x in data:

        print(x * (2020-x))
        break
    
for m, x  in enumerate(data):

    s = 2020 - x    

    for n, y in enumerate(data[m+1:]):
        
        if s - y in data:

            print(x * y * (s-y))
            break