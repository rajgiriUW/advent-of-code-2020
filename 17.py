# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:51:07 2020

@author: Raj
"""
import numpy as np
import itertools
base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/17_energy.txt')
data = []
for d in f.readlines():
    d = d.strip()
    data.append([int(x) for x in d.replace('#', '1').replace('.', '0')])

test_data = np.array(data)
r, c = test_data.shape
pad = 7
test_field = np.zeros((r+2*pad, r+2*pad, r+2*pad))
center = test_field.shape[0]//2
width = r //2 
test_field[center, center-width:center+width, center-width:center+width] = test_data[:]

rows, cols, height = test_field.shape
coords = np.array(list(itertools.product(range(1, rows-1), 
                                         range(1, cols-1), 
                                         range(1, height-1))))

cycles = 6
for cycle in range(cycles):
    
    test_field_new = np.zeros(test_field.shape) * 0
    for cd in coords:
        # print(cd)
        r, c, z = cd
        cube = test_field[r][c][z]
        if cube == 1:
            test_field_new[r][c][z] = 2 <= np.sum(test_field[r-1:r+2, c-1:c+2, z-1:z+2]) - cube <= 3
                
        else:
            test_field_new[r][c][z] =  np.sum(test_field[r-1:r+2, c-1:c+2, z-1:z+2]) - cube == 3
    test_field = np.copy(test_field_new)
            
print(np.sum(test_field))    
    
# Part 2
test_data = np.array(data)
r, c = test_data.shape
pad = 7
test_field = np.zeros((r+2*pad, r+2*pad, r+2*pad, r+2*pad))
center = test_field.shape[0]//2
width = r //2 
test_field[center, center-width:center+width, center-width:center+width, center] = test_data[:]


rows, cols, height, depth = test_field.shape
coords = np.array(list(itertools.product(range(1, rows-1), 
                                         range(1, cols-1), 
                                         range(1, height-1),
                                         range(1, depth-1))))

cycles = 6
for cycle in range(cycles):
    
    test_field_new = np.zeros(test_field.shape) * 0
    for cd in coords:
        # print(cd)
        r, c, z, w = cd
        cube = test_field[r][c][z][w]
        if cube == 1:
            test_field_new[r][c][z][w] = 2 <= np.sum(test_field[r-1:r+2, c-1:c+2, z-1:z+2, w-1:w+2]) - cube <= 3
                
        else:
            test_field_new[r][c][z][w] =  np.sum(test_field[r-1:r+2, c-1:c+2, z-1:z+2, w-1:w+2]) - cube == 3
    test_field = np.copy(test_field_new)
            
print(np.sum(test_field))    