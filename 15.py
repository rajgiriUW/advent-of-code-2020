# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:20:13 2020

@author: Raj
"""

import time

# Dict version might be faster

t = time.time()
data = [18,8,0,5,4,1,20]

def elves(end):
    
    datadict = {}
    for n, k in enumerate(data):
        datadict[k] = [n, n]
    
    target = data[-1]
    n = len(data)
    while n < end:
        
        idx = datadict[target][1] - datadict[target][0]
        if idx not in datadict:
            datadict[idx] = [n, n]
        else:
            datadict[idx] = [datadict[idx][1], n]
       
        target = idx
        n += 1
    
    return target

print(elves(2020), time.time() - t)
t = time.time()
print(elves(30000000), time.time() - t)

# First version
while n < end:
    
    if data[n-1] in data[n-2::-1]:
        
        idx = data[n-2::-1].index(data[n-1])
        idx = len(data) - idx - 1
        data.append(n-idx)
    else:
        data.append(0)
        
    n += 1

# print(data[end-1])