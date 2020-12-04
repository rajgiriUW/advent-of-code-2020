# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:03:09 2020

@author: Raj
"""


base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/04_passports.txt')
data = f.read().split('\n\n')
data.append('\n') # add missing end character

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
ppt = {}

for line in data:
    
    is_valid = True
    for k in line.replace('\n', ' ').split(' '):
        if any(k):
            x, y = k.split(':')
            ppt.update([(x, y)])
        
    for k in keys:
        if k not in ppt:
            is_valid = False
            break
        
    valid += is_valid
    ppt = {}
    
print(valid)

# Part 2
def valid_ppt(key, val):
    
    if key == 'byr':
        return 1920 <= int(val) <= 2002
    elif key == 'iyr':
        return 2010 <= int(val) <= 2020
    elif key == 'eyr':
        return 2020 <= int(val) <= 2030
    elif key == 'pid':
        if len(val) == 9:
            return sum([k.isdigit() for k in val]) == 9
        else:
            return False
    elif key == 'hcl':
        if val[0] == '#' and len(val[1:]) == 6:
            return sum([k.isdigit() or k.isalpha() for k in val[1:]]) == 6
        else:
            return False
    elif key == 'hgt':
        if val.endswith('cm'):
            return 150 <= int(ppt['hgt'] [:-2]) <= 193
        elif val.endswith('in'):
            return 59 <= int(ppt['hgt'] [:-2]) <= 76
    elif key == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    return False

valid = 0
ppt = {}

for line in data:
    
    is_valid = True
    for k in line.replace('\n', ' ').split(' '):
        if any(k):
            x, y = k.split(':')
            ppt.update([(x, y)])
        
    for k in keys:
        if k not in ppt:
            is_valid = False
            break
        elif not valid_ppt(k, ppt[k]):
            is_valid = False
            break
    valid += is_valid
    ppt = {}

print(valid)