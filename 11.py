# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:56:00 2020

@author: Raj
"""

import numpy as np
import itertools

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/11_seats.txt')
_seats = f.read().split('\n')[:-1]

seats = np.zeros((len(_seats), len(_seats[0])))

for n, s in enumerate(_seats):
    
    s = list(s.replace('L', '0').replace('.', '2'))
    seats[n] = [int(x) for x in s]
    seats[n][seats[n] == 2] = np.nan

seats = np.pad(seats, 1, 'constant', constant_values = 0) # add boundaries

def seat_state(seats, r, c):
    
    if seats[r][c] == np.nan:
        return np.nan
    
    elif seats[r][c] == 1:
        return np.nansum(seats[r-1:r+2, c-1:c+2]) - seats[r][c] < 4
            
    elif seats[r][c] == 0:
        return np.nansum(seats[r-1:r+2, c-1:c+2]) - seats[r][c] == 0

def find_seats(seats):
    
    num_occ = 0
    num_occ_pre = -1
    rows, cols = seats.shape
    
    while num_occ != num_occ_pre:
        
        seats_co = np.copy(seats)
        num_occ_pre = int(np.nansum(seats))    
        for r in range(1, rows-1):
            
            seats_co[r, 1:cols-1] = [seat_state(seats, r, y) for y in range(1, cols-1)]
            
        seats = seats_co[:]
        num_occ = int(np.nansum(seats))    
    
    return num_occ

print(find_seats(seats))
    
# Part 2
def non_floor(seats, r, c, vector):
    ''' vector = [x, y] e.g. [-1, -1] = down-left direction'''
    delx, dely = vector
    
    if delx == 0: #vertical
        arr = seats[r+dely::dely, c]
        
    elif dely == 0: #horizontal
        arr = seats[r, c+delx::delx]
    
    else:
        arr = np.diag(seats[r+dely::dely, c+delx::delx])
    
    return arr[np.where(np.isfinite(arr))][0]
    
vectors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
def seat_state(seats, r, c):
    
    if seats[r][c] == np.nan:
        return np.nan
    
    elif seats[r][c] == 1:
        return sum([non_floor(seats, r, c, v) for v in vectors]) < 5
            
    elif seats[r][c] == 0:
        return sum([non_floor(seats, r, c, v) for v in vectors]) == 0

print(find_seats(seats))
