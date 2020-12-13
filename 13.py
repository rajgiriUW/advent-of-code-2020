# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:59:54 2020

@author: raj
"""

import numpy as np
from functools import reduce
from operator import mul

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/13_buses.txt')
data = f.read().split('\n')[:-1]

leave = int(data[0])
buses = [int(b) for b in data[1].split(',') if b.isnumeric()]
times = np.array([b * ((leave // b) + 1) for b in buses])

print(buses[np.argmin(times - leave)] * np.min(times - leave))

# Part 2
offsets = [n for n, d in enumerate(data[1].split(',')) \
                    if d.isnumeric() and int(d) in buses]

# Gave up and saw on Reddit that people were using "Chinese Remainder Theorem
# something I'd never heard of! But following rubric from here:
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/crt.pdf

def inv(x, m): return pow(x,m-2,m) # don't have Python 3.8

remainders = [b - o for b, o in zip(buses, offsets)]
remainders[0] = 0
for n, r in enumerate(remainders):
    if r < 0:
        remainders[n] = buses[n] - np.mod(offsets[n], buses[n])
_pd = reduce(mul, buses)
m_arr = [int(_pd / b) for b in buses]
y_arr = [inv(m, b) for m, b in zip(m_arr, buses)]
crt = []
for r, m, y in zip(remainders, m_arr, y_arr):
    crt.append(r*m*y)
print(crt, sum(crt) % _pd)
