# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 23:45:05 2020

@author: Raj
"""


import numpy as np
import copy
base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/22_combat.txt')
data = f.read().split('\n\n')

# bottom of deck is at 0, top is at -1
p1 = [int(x) for x in data[0].split('\n')[1:]][::-1]
p2 = [int(x) for x in data[1].split('\n')[1:-1]][::-1]
players = [p2, p1]

def play(p1, p2, p1_card, p2_card):
    
    if p1_card > p2_card:
        p1.insert(0, p1_card)
        p1.insert(0, p2_card)
    
    else:
        p2.insert(0, p2_card)
        p2.insert(0, p1_card)

def combat():

    while len(p1) != 0 and len(p2) != 0:
        p1_card, p2_card = [p1.pop(), p2.pop()]
        play(p1, p2, p1_card, p2_card )
    
    winner = p1 if len(p1) > 0 else p2
    
    return winner == p1 # 1 = p1, 0 = p2

def recur_combat(p1, p2):
    
    pairs = {}
    while len(p1) != 0 and len(p2) != 0:
        
        # print(p1[::-1],'\n',p2[::-1])
        p1key = ''.join(str(p1))
        p2key = ''.join(str(p2))
        
        if p1key in pairs and p2key in pairs: 

            p1_card, p2_card = [p1.pop(), p2.pop()]
            
            p1.insert(0, p1_card)
            p1.insert(0, p2_card)
            
            winner = p1
            return winner == p1
        
        # Tuples weren't working, use a dict and find unique keys
        pairs[p1key] = None
        pairs[p2key] = None
        
        p1_card, p2_card = [p1.pop(), p2.pop()]
        
        if p1_card <= len(p1) and p2_card <= len(p2):
            
            p1_new = copy.deepcopy(p1[-p1_card:])
            p2_new = copy.deepcopy(p2[-p2_card:])
            
            winner = recur_combat(p1_new, p2_new)
            
            if not winner: # 0 = p2 wins
                p2.insert(0, p2_card)
                p2.insert(0, p1_card)
            else:
                p1.insert(0, p1_card)
                p1.insert(0, p2_card)
                
        else:
            play(p1, p2, p1_card, p2_card)
    
    winner = p1 if len(p1) > 0 else p2

    return winner == p1 # 1 = p1, 0 = p2

winner = players[combat()]
print('Part 1' ,np.arange(1, len(winner)+1) @ np.array(winner))

# Reload data
p1 = [int(x) for x in data[0].split('\n')[1:]][::-1]
p2 = [int(x) for x in data[1].split('\n')[1:-1]][::-1]
players = [p2, p1]

winner = players[recur_combat(p1, p2)]
print('Part 2', np.arange(1, len(winner)+1) @ np.array(winner))
