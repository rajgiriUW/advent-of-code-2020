# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:03:23 2020

@author: Raj
"""


# import numpy as np
# import pandas as pd
# base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
# data = pd.read_csv(base + r'/02_file.txt', header=None, sep=' ')

# valid = 0
# for k in data.index:
    
#     lo, hi = [int(x) for x in data[0].loc[k].split('-')]
#     lt = data[1].loc[k].split(':')[0]
    
#     if sum(lt == y for y in data[2].loc[k]) in range(lo, hi+1):
#         valid += 1

# print(valid)

# # part 2

# valid = 0

# for k in data.index:
    
#     lo, hi = [int(x)-1 for x in data[0].loc[k].split('-')] #-1 for 1-dex
#     lt = data[1].loc[k].split(':')[0]
    
#     password = data[2].loc[k]
#     if password[lo] != lt and password[hi] == lt:
#         valid += 1
#     elif password[lo] == lt and password[hi] != lt:
#         valid += 1

# print(valid)

# Non Pandas, non-numpy


base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
with open(base + r'/02_file.txt') as f:
    
    valid = 0
    for line in f:
        
        data = line.split(' ')
        
        lo, hi = [int(x) for x in data[0].split('-')]
        lt = data[1].split(':')[0]
       
        if sum(lt == y for y in data[2]) in range(lo, hi+1):
            valid += 1

print(valid)    

start_time = time.time()
with open(base + r'/02_file.txt') as f:
    
    valid = 0
    for line in f:
        
        data = line.split(' ')
        
        lo, hi = [int(x)-1 for x in data[0].split('-')]
        lt = data[1].split(':')[0]
        
        password = data[2]
        if password[lo] != lt and password[hi] == lt:
            valid += 1
        elif password[lo] == lt and password[hi] != lt:
            valid += 1
            
print(valid)
