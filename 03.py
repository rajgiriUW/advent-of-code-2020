# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:17:15 2020

@author: Raj
"""

import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'

f = open(base + r'/03_map.txt')
tmap = np.array([x.split('\n')[0] for x in f.readlines()])
    
trees = 0
for n, line in enumerate(tmap):
    
    xpos = (3 * n) % len(line)
    trees +=  line[xpos] == '#'
    
print(trees)        

# Part 2
xs = [1, 3, 5, 7, 1]
ys = [1, 1, 1, 1, 2]

trees = np.zeros(5)

for m, del_x, del_y in zip(range(5), xs, ys):

    row = 0
    for n, line in enumerate(tmap):
        
        if n % del_y != 0:
            continue
        
        xpos = (del_x * row) % len(line)
        trees[m] +=  line[xpos] == '#'
        # print(n, xpos, line,line[xpos] == '#' )
        row += 1
    
print(int(np.product(trees)))
