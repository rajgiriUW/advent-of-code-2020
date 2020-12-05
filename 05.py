# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:06:18 2020

@author: Raj
"""

import numpy as np 

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/05_seats.txt')

data = f.read().split('\n')[:-1] # drop last empty row

def to_bin(line):
    
    row = []
    for l in line[:-3]:
        row.append('0') if l == 'F' else row.append('1')
    
    col = []
    for l in line[-3:]:
        col.append('0') if l == 'L' else col.append('1')
        
    return ''.join(row), ''.join(col)

def to_seat(d):
    
    row, col = [int(k, 2) for k in to_bin(d)]
    return row*8 + col

result = np.array(list(map(to_seat, data)))
print(np.max(result))

# part 2
result = np.sort(result)
missing = np.argmax(np.diff(result))

print(result[missing] + 1) # seat is next missing one

