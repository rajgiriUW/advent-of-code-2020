# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:35:46 2020

@author: raj
"""
import itertools

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/09_codebreaking.txt')
data = f.read().split()
data = [int(x) for x in data]

rang = 25
for n, d in enumerate(data[rang:], start=rang+1):
    
    sums = map(sum, itertools.combinations(data[n-1-rang:n-1], 2))
    if d not in list(sums):
        print('Element', n, '; number', d)
        break
    
# part 2
target = 50047984
end = len(data)
for n, d in enumerate(data):
    
    for m in range(n+1, end - n):
        
        if sum(data[n:m]) == target:
            print('Smallest\t', min(data[n:m]))
            print('Largest\t', max(data[n:m]))
            print('Sum\t', min(data[n:m]) + max(data[n:m]))
            break
        
        