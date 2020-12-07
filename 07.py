# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:03:55 2020

@author: Raj
"""

import pandas as pd
import re
import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/07_bags.txt')
data = f.read().split('\n')[:-1]

# Get all colors
colors = []
for d in data:
    
    cl = d.split('contain')[0].split('bag')[0][:-1]
    colors.append(cl)
    
df = pd.DataFrame(0, index = colors, columns = colors)    

# Define bags rule per line
def bag_rule(line):
    
    rules = line.split('contain')
    parent = rules[0].split('bag')[0][:-1].strip()
    children = rules[1].split('bag')
    for c in children:
        
        c = c.strip()
        r = re.search('\d\s', c)
        if r:
            st, sp = r.start(), r.end()
            num = int(c[st:sp])
            cl = c[sp:]
            df[parent][cl] = num
        
# Find all color rules
for d in data:
    
    bag_rule(d)
    
# What does a bag contain
def bag_has(color):
    
    return df[color].iloc[df[color].to_numpy().nonzero()]

# What contain this bag color
def contain_bag(color):
    
    return df.columns[df.loc[color].to_numpy().nonzero()]

# Which bags contain gold directly
contain_gold = contain_bag('shiny gold').values

# keep calling until no longer any change in bags containing gold eventually
colors_with_gold = np.array(contain_gold)
values = 0
values_pre = -1
while values != values_pre:
    
    values_pre = colors_with_gold.shape
       
    for c in colors_with_gold:
   
        colors_with_gold = np.union1d(colors_with_gold, contain_bag(c).values)
        
    values = colors_with_gold.shape
    
print(values)

# Part 2
def bag_has_rec(color, n = 1):

    values= 1
    for cl, val in bag_has(color).to_dict().items():
        values += val * bag_has_rec(cl, val)
            
    return values       
    
print(bag_has_rec('shiny gold') - 1) # subtract the bag itself
