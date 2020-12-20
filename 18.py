# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:19:19 2020

@author: Raj
"""

from operator import add, mul
import re

base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/18_math.txt')
data = f.read().split('\n')[:-1]

# once there are two numbers, perform the most recent operation on stack
# if parenthesis, need two more numbers to perform its operation first
# if right parenthesis, if previous two are numbers, operate. Else keep going
def eval_eq(line):
    
    line = line.strip().replace(' ', '') 
    
    nums = []
    ops = []
    nnum = 0
    operands = {'+': add, '*': mul}
    for c in line:
        # cl = iter(list(line))
        # c = next(cl)
        # print(c, nums, ops, nnum)
        if c == '(':
            nnum = 0
            nums.append('(')
        elif c == ')':
            for x in [nums.pop(), nums.pop()]:
                if x != '(':
                    nums.append(x)
                    nnum += 1
        elif c.isnumeric():
            nums.append(int(c))
            nnum += 1
        elif c in operands:
            ops.append(operands[c])
        if nnum >= 2 and len(nums) > 1 and '(' not in nums[-2:]:
            nums.append(ops.pop()(nums.pop(), nums.pop()))
            nnum -= 1    
        # print(c, nums, ops, nnum, operations)
    return nums[0]

print(sum(list(map(eval_eq, data))))

# Part 2
# Sneaky Raj with a sneaky idea. Let's make a new class, change how * and + are
# defined, and then swap those operators. Let native Python handle the PMDAS
class newmath:
    
    def __init__(self, val):
        
        self.val = val
    
    def __add__(self, addend):
        
        return newmath(self.val * addend.val)
    
    def __mul__(self, multiplicand):

        return newmath(self.val + multiplicand.val)


def eval_eq_addprec(line): #addition precedence
    
    # Create as classes of above, and swap the operators
    line = line.strip().replace(' ', '') 
    newline = []
    num_idx = [r.span()[0] for r in re.finditer('\d', line)]
    for n, c in enumerate(line):
        
        if n in num_idx:
            newline.append('newmath(' + c + ')')
        elif c == '*':
            newline.append('+')
        elif c == '+':
            newline.append('*')
        else:
            newline.append(c)
            
    newline = ''.join(newline)

    return eval(newline).val

print(sum(list(map(eval_eq_addprec, data))))
