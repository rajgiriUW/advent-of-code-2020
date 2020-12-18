# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:01:46 2020

@author: raj
"""
import numpy as np
base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/16_train.txt')
data = f.read().split('\n\n')

rules = data[0].split('\n')
yours = [int(x) for x in data[1].split('\n')[1].split(',')]
tckt = data[2].split('\n')[1:-1]
tickets = []
for t in tckt:
    tickets.append([int(x) for x in t.split(',') ])

# Rules per field code
rulesd = {}
total_rules = 0
for r in rules:
    k = r.split(':')[0]
    rnges = [rn.strip() for rn in r.split(':')[1:][0].split('or')]
    v = []
    for rn in rnges:
        
        rni = tuple([int(x) for x in rn.split('-')])
        v.append(range(rni[0], rni[1]+1))
        total_rules += 1
    rulesd[k] = v

# If number not in any range, the not_found will be equal to total_rules #
# Discards added to Part 2
error_rate = 0
discards = []
for d, t in enumerate(tickets):

    for n in t:    
        not_in_range = 0
        for r in rulesd:
            for rn in rulesd[r]:
                not_in_range += (n not in rn)
                
        if not_in_range >= total_rules:
            error_rate += n
            discards.append(d)

print(error_rate)

# Part 2
valid_tickets = np.array(tickets)
valid_tickets = np.delete(valid_tickets, np.array(discards), axis=0)

# dict with possible locations per field
locsd = dict.fromkeys(rulesd.keys())
for k in locsd:
    locsd[k] = set()

# Find valid locations per field, update with intersection of possibilities per ticket
for t in valid_tickets:
    for r in rulesd:
        fields = []
        for x, n in enumerate(t):
        
            for rn in rulesd[r]:
                if n in rn:
                    fields.append(x)
                    
        if any(locsd[r]):
           locsd[r] = locsd[r].intersection(fields)
        else:
           locsd[r] = set(fields)

# One location is found, use that to find the others, convert from set to ints
all_found = False
remove = [] # once we've found a particular field
while not all_found:
    for r in rulesd:
        if len(locsd[r]) == 1:
            idx = list(locsd[r])[0]
            if idx not in remove:
                remove.append(idx)
            continue
        else:
            for rm in remove:
                locsd[r].discard(rm)
    if len(remove) == len(locsd) - 1:
        all_found = True
locsd = dict(zip(locsd.keys(), [int(list(x)[0]) for x in locsd.values()]))

# Find departure keys
dep_keys = []
for d in locsd.keys():
    if d.startswith('departure'):
        dep_keys.append(d)

# Answer the damn question
yours_dep = 1
for d in dep_keys:
    
    yours_dep *= yours[locsd[d]]

print(yours_dep)