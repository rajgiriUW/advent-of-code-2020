# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:18:15 2020

@author: Raj
"""



base = r'C:/Users/Raj/OneDrive/UW Work/Coding and Signal Processing Work/Python/aoc_2020/'
f = open(base + r'/08_assembly.txt')
data = f.read().split('\n')[:-1]

accumulator = 0
command_lines = []  #line numbers, 
line = 0
while line not in command_lines:
    
    cmd, val = data[line].split()
    val = int(val)
    command_lines.append(line)
    
    line = exec_cmd(cmd, val, line)

print(accumulator)
    
def exec_cmd(cmd, val, line):
    
    if cmd == 'jmp':
        return line + val
    elif cmd == 'acc':
        global accumulator
        accumulator += val
    return line + 1

# part 2
nop_lines = []
jmp_lines = []
accumulator = 0
for n, d in enumerate(data):
    
    op = d.split()[0]
    if op == 'nop':
        nop_lines.append(n)
    elif op == 'jmp':
        jmp_lines.append(n)
        
def test_code(change_line = -1):
    
    global accumulator 
    accumulator = 0
    command_lines = []  #line numbers, 
    line = 0
    flip = {'nop': 'jmp', 'jmp':'nop'}
    while line not in command_lines and line < len(data):
        
        cmd, val = data[line].split()
        val = int(val)
        if line == change_line:
            cmd = flip[cmd]
        command_lines.append(line)
        
        line = exec_cmd(cmd, val, line)

    return accumulator, line >= len(data)

# Test nops
for nops in nop_lines:
    accum, success = test_code(change_line = nops)
    if success:
        print(accum)
        break
    
for jmps in jmp_lines:
    
    accum, success = test_code(change_line = jmps)
    if success:
        print(accum)
        print(jmps)
        break
