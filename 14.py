# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:44:32 2020

@author: Raj
"""

import re

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/14_bitmask.txt')
data = [d.rstrip() for d in f.readlines()]

def bitmask(memory, mask, address, value):
    
    if address not in memory:
        memory[address] = f'{0:b}'.zfill(36)
    value = bin(value)[2:].zfill(36)
    result = []
    for n in range(36):
        result.append(value[n] if mask[n] == 'X' else mask[n])
    
    memory[address] = ''.join(result)
    
    return 
        
def int2(binstr):
    
    return int(binstr, 2)
    
def decoder(memory, mask, address, value):
    
    addr = []
    addrb = bin(int(address))[2:].zfill(36)
    for n in range(36):
        if mask[n] != 'X':
            addr.append(str(int(mask[n]) | int(addrb[n]) ) )
        else:
            addr.append('X')
    addr = ''.join(addr)
    
    bits = [r.span()[0] for r in re.finditer('X', addr)]
    xs = [bin(x)[2:].zfill(len(bits)) for x in range(2**len(bits))]
    for x in xs:
        addrx = list(addr)
        for n, b in enumerate(bits):
            addrx[b] = x[n]
        address = int(''.join(addrx), 2)
        bitmask(memory, xmask, address, value)
    
    return 

memory = {}
memory_2 = {}
xmask = ''.zfill(36).replace('0','X')

for d in data:
    if 'mask' in d:
        mask = d.split('= ')[-1]
    else:
        s = d.split()
        value = int(s[-1])
        address = re.search(r'\d+\D', s[0]).group(0)[:-1]
        bitmask(memory, mask, address, value)
        decoder(memory_2, mask, address, value)
        
print(sum(list(map(int2, memory.values()))))
print(sum(list(map(int2, memory_2.values()))))