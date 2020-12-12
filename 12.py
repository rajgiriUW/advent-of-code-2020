# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:13:30 2020

@author: raj
"""
import re
import numpy as np

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/12_directions.txt')
directions = f.read().split('\n')[:-1]

heading = 'E' # 0 = N, 1 = E, 2 = S, 3 = W
loc = [0, 0]

#N, S, E, W, L, R, F
def turn(heading, path, units):
    
    turns = {90: 1, 180: 2, 270:3}
    angle = {'L': -1, 'R': 1}
    headings = ['N', 'E', 'S', 'W']
    cardinals = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    
    return headings[(cardinals[heading] + angle[path]*turns[units]) % 4]

def move(heading, path, units, loc):
    '''N, S, E, W motion '''
    
    motion = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    
    if path == 'F':
        delx, dely = [units * x for x in motion[heading]]
    else:
        delx, dely = [units * x for x in motion[path]]
    loc[0] += delx
    loc[1] += dely
    
    return loc

for d in directions:
    # print(d, loc, heading)
    path, units = [re.split('\d', d)[0], int(re.split('\D', d)[-1])]
    
    if path in ['L', 'R']:
        heading = turn(heading, path, units)
    else:
        loc = move(heading, path, units, loc)
    # print('-->',loc, heading)

print(loc, sum(np.abs(loc)))

#Part 2
def move_to(path, units, loc, waypoint):
    '''N, S, E, W motion '''
    
    motion = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    
    if path == 'F':
        x = units * (waypoint - loc)
        loc += x
        waypoint += x

    else:
        waypoint += np.array([units * x for x in motion[path]])
    
    return loc, waypoint

def rotate(path, units, loc, waypoint):
    
    x, y = waypoint - loc
    turns = {90: [y, -x], 180: [-x, -y], 270: [-y, x]}
    angle = {'L': -1, 'R': 1}
    if units == 180:
        waypoint = np.array(turns[units])
    else:
        waypoint = np.array([angle[path] * k for k in turns[units]])
    
    return waypoint + loc
  
waypoint = np.array([10, 1]) # always relative to loc
loc = np.array([0, 0])  
for d in directions:
    print(d, loc, waypoint)
    path, units = [re.split('\d', d)[0], int(re.split('\D', d)[-1])]
    
    if path in ['L', 'R']:
        waypoint = rotate(path, units, loc, waypoint)
    else:
        loc, waypoint = move_to(path, units, loc, waypoint)
    print('-->',loc, waypoint)
    
print(loc, sum(np.abs(loc)))