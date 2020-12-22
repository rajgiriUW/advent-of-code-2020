# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:17:02 2020

@author: Raj
"""

import numpy as np
from operator import mul
from functools import reduce

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/20_tiles.txt')
data = f.read().split('\n\n')[:-1]
tiles = {}
edges = [] # pattern matching, these hold strings
edges_r = []

# Make numeric and store in dict
for d in data:
    k, t = d.split(':')
    k = int(k.split()[-1])
    t = t.strip().split('\n')
    tile = np.zeros((len(t), len(t[0])))
    for n, tl in enumerate(t):
        tile[n,:] = np.array([s == '#' for s in tl])
    tiles[k] = Tile(tile.astype(int), idx=k)
    
    for e, r in zip(tiles[k].edg, tiles[k].edg_r):
        edges.append(''.join([str(x) for x in e.astype(int)]))
        edges_r.append(''.join([str(x) for x in r.astype(int)]))

import copy
tilesbu = copy.deepcopy(tiles)

class Tile:
    
    def __init__(self, arr, angle = 0, mirror = '', idx = 0):
        # angle = CCW of [0, 90, 180, 270]
        # mirror = ['', 'X', 'Y'] = none, horiz, vert
        self.arr = arr
        self._arr = arr[:]
        self.edg = self.edges()
        self.edg_r = self.edges(rev=-1)
        self.angle = angle
        self.mirror = mirror
        self.neighbors = set() # neighbors right, up, left, down (CCW)
        self.edge_map = {0:None, 1:None, 2:None, 3:None}
        self.idx = idx
    
    def edges(self, rev=1):
        '''rev=-1 = flip(lr), edges are right, top, left, bottom'''
        return list([self.arr[:, -1][::rev], self.arr[0, :][::rev],
                     self.arr[:, 0][::rev], self.arr[-1, :][::rev]])

    def rot(self, angle):
        
        self.angle = (self.angle + angle) % 360
        for i in range(angle // 90):
            self.arr = np.rot90(self.arr)
            
        self.edg = self.edges()
        self.edg_r = self.edges(rev=-1)
        
        if angle == 90:
            mapd = {0:1, 1:2, 2:3, 3:0}
        elif angle == 180:
            mapd = {0:2, 1:3, 2:0, 3:1}
        elif angle == 270:
            mapd = {0:3, 1:0, 2:1, 3:2}
        elif angle == 0:
            mapd = {0:0, 1:1, 2:2, 3:3}
            
        cp = copy.deepcopy(self.edge_map)
        for k, v in mapd.items():
            self.edge_map[v] = cp[k]
        del cp
    
        return 
    
    def flip(self, mirror):
        # note that XY mirror = flip + rot90 twice
        if mirror == '':
            return
        else:
            #restore first to not accidentally mirror tiwce
            if mirror == 'X':
                self.arr = np.fliplr(self.arr)
                self.mirror = 'X'
                temp = self.edge_map[0]
                self.edge_map[0] = self.edge_map[2]
                self.edge_map[2] = temp
            elif mirror == 'Y':
                self.arr = np.flipud(self.arr)
                self.mirror = 'Y'
                temp = self.edge_map[1]
                self.edge_map[1] = self.edge_map[3]
                self.edge_map[3] = temp
       
        self.edg = self.edges()
        self.edg_r = self.edges(rev=-1)
        
        return        

def neighbors(t1, t2): 
    '''Compare left tile against right tile, flip and rotate and determine 
    if it ever matches '''
    
    if len(t1.neighbors) == 4:
        return t1.neighbors
    
    for n, edg in enumerate(t1.edg):
        
        for m, edg2 in enumerate(t2.edg):
            if np.allclose(edg, edg2):
                t1.neighbors.add(t2.idx)
                t2.neighbors.add(t1.idx)
                
                for k, v in t1.edge_map.items():
                    if v == t2.idx:
                        t1.edge_map[k] = None
                        break
                for k, v in t2.edge_map.items():
                    if v == t1.idx:
                        t2.edge_map[k] = None
                        
                t1.edge_map[n] = t2.idx
                t2.edge_map[m] = t1.idx
                return t1.neighbors

        for n, edg in enumerate(t1.edg_r):
            for m, edg2 in enumerate(t2.edg):
                if np.allclose(edg, edg2):
                    t1.neighbors.add(t2.idx)
                    t2.neighbors.add(t1.idx)
                    t1.edge_map[n] = t2.idx
                    t2.edge_map[m] = t1.idx
                    
                    if n == 1 or n == 3:
                        t1.flip('X')
                    else:
                        t1.flip('Y')
                
                    return t1.neighbors

    return 0

corners = []
edges = []
centers = []
for _, t1 in tiles.items():
    for idx, tile in tiles.items():
        if t1.idx != idx: #skip equal pairs
            neighbors(t1, tile)

for _, t1 in tiles.items():
    if len(t1.neighbors) == 4:
        centers.append(t1.idx)
    elif len(t1.neighbors) == 3:
        edges.append(t1.idx)
    elif len(t1.neighbors) == 2:
        corners.append(t1.idx)
        
print(reduce(mul, corners))

# Part 2: There be monsters!!

# Step 1, assemble the image
rows = 10
cols = 10
sz = 12

tiles[corners[0]].rot(270) # to correct mirroring error

for c in corners:
    print(c, tiles[c].edge_map)
    
    if tiles[c].edge_map[0] == tiles[c].edge_map[3] == None:
        bot_right = c
    elif tiles[c].edge_map[0] == tiles[c].edge_map[1] == None:
        top_right = c
    elif tiles[c].edge_map[2] == tiles[c].edge_map[1] == None:
        top_left = c
    elif tiles[c].edge_map[2] == tiles[c].edge_map[3] == None:
        bot_left = c

def construct(tile_img, pixel):
    
    for k, e in tile_img[pixel[0], pixel[1]].edge_map.items():
        
        if e:
            # shares right edge 
            if k == 0:
                r, c = [0, 1]
            
            # shares top
            elif k == 1:
                r, c = [-1, 0]
            
            # shares left edge
            elif k == 2:
                r, c = [0, -1]
            
            # shares bottom
            elif k == 3:
                r, c = [1, 0]
            
            pixel[0] += r
            pixel[1] += c
            
            if -1 in pixel or 12 in pixel:
                print('error')
                return None
            
            print(e, pixel)
            if tile_img[pixel[0], pixel[1]] == None:
                tile_img[pixel[0], pixel[1]] = tiles[e]

            pixel[0] -= r
            pixel[1] -= c
            
            next_tiles.append(e)
            
    return 1

pixel = [0, sz-1] # top-right
tile_img = np.empty((sz, sz), dtype=Tile)
tile_img[pixel[0], pixel[1]] = tiles[top_right]
# tile_img[0, 10] = tiles[tile_img[0, 11].edge_map[2]]
# tile_img[1, 11] = tiles[tile_img[0, 11].edge_map[3]]

for r in range(sz-1):
    
    for c in range(sz-1, 0, -1):
    
        pixel = [r, c]
        print(pixel)

        if r == 0:
            
            while tile_img[r,c].edge_map[1] != None:
                print('error')
                tile_img[r,c].rot(270)
                
        if r == 11:
            while tile_img[r,c].edge_map[3] != None:
                print('error')
                tile_img[r,c].rot(270)
                
        if c == 0:
            while tile_img[r,c].edge_map[2] != None:
                print('error')
                tile_img[r,c].rot(270)
        
        if c == 11:
            while tile_img[r,c].edge_map[0] != None:
                print('error')
                tile_img[r,c].rot(270)

        if c > 0:        
            tile_img[r, c-1] = tiles[tile_img[r, c].edge_map[2]]
        if r < 11:
            tile_img[r+1, c] = tiles[tile_img[r, c].edge_map[3]]
        
        if tile_img[r, c-1].edge_map[0] != tile_img[r, c].idx:
            
            tile_img[r,c -1].flip('X')
            print(tile_img[r, c-1].edge_map, tile_img[r, c].edge_map)
            print(tile_img[r, c-1].idx, tile_img[r, c].idx)

        
        if tile_img[r, c-1].edge_map[0] != tile_img[r, c].idx:
            print('errrr')
            tile_img[r,c -1].flip('X')
        
        print(tile_img[r, c].edge_map)
        
        if r > 0:
            
            while tile_img[r,c].edge_map[1] != tile_img[r-1, c].idx:
                print('error')
                tile_img[r,c].rot(270)
            
# We'll pick one corner, propagate from there
def plot_img(tile_img):
    sz = 12
    rows = 10
    cols = 10
    img = np.zeros((rows * sz, cols * sz))
    for r in range(rows):
        
        for c in range(cols):
            
            img[r * sz: (r+1) * sz, c * sz, (c+1) * sz] = tile_img[r, c].arr

    return img

