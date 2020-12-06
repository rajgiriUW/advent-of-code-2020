# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:02:39 2020

@author: Raj
"""
import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/06_questions.txt')

data = f.read().split('\n\n') # drop last empty row

counts = 0 
for d in data:
    
    l = np.array([k for k in d.replace('\n', '')])
    counts += np.sum(len(np.unique(l)))
    
print(counts)

# part 2
counts = 0

def spl_ar(line):
    
    return np.array([k for k in line])

for d in data:
    
    line = d.split('\n')
    
    first = spl_ar(line[0])
    for l in line[1:]:
        if any(l): # last line has an extra carriage return
            first = np.intersect1d(first, spl_ar(l))
        
    counts += len(first)
    
print(counts)   