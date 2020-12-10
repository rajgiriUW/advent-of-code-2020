# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:53:26 2020

@author: Raj
"""

import numpy as np
import re 

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/10_jolts.txt')
data = f.read().split('\n')[:-1]

data = [int(x) for x in data]
datas = np.sort(data)
datas = np.insert(datas, 0, 0)
datas = np.append(datas, np.max(datas) + 3)
jumps = np.diff(datas)

print( len(np.where(jumps == 3)[0]) * len(np.where(jumps == 1)[0]))

# part 2
# Count number of 1 sequences. 3 1's = 2 different arrangements, 4 = 4, 5 = 6
# 3113, 31113, 311113, 3111113

sjumps = ''.join([str(j) for j in jumps])
sjumps = '3' + sjumps

def subs(string, pattern):
    
    return len([i for i in range(len(string)) if string.startswith(pattern, i)])
        
print(7 ** subs(sjumps, '311113') * (4 ** subs(sjumps, '31113')) * (2 ** subs(sjumps, '3113'))) 
