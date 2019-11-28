# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:01:59 2019

@author: James
"""

#!/usr/bin/env python3

import sys

debug = False

try:
    if sys.argv[1] == "-d": 
        debug = True
        path = sys.argv[2]
    else:
        path = sys.argv[1]        
except IndexError:
    print("Please specify a file.")
    sys.exit()

try:
    assert ".tex" in path
    with open(path, "r") as file:
        lines = file.read()     
except AssertionError:
    print("Please specify a .tex file.")
    sys.exit()
except IOError:
    print("Please specify an existing file.")
    sys.exit()
    
if debug:
    print("\nStarting text: " + str(lines)+"\n\n")
    
    
def remove_latex(e, line):
    if ("{" in e or "[" in e) and e in line:
        start = line.find(e)
        end = line.find("}")
        line = line.replace(line[start:end+1], "")
        line = remove_latex(e, line)
    elif e in line:
        line = line.replace(e, "")
    return line


DEL_LIST = ['\n',
            '\t',
            '\\title{',
            '\\author{',
            '\\documentclass[',
            '\\begin{',
            '\\end{',
            '\\cite{',
            '\\section{',
            '\\section*{',
            '\\usepackage{',
            '\\bibliographystyle{',
            '\\bibliography{',
            '\\maketitle']
    
lines = lines.splitlines()
for i in range(len(lines)):
    for e in DEL_LIST:
        if e in lines[i]:
            lines[i] = remove_latex(e, lines[i])
        
lines = list(filter(None, lines))

lines = " ".join(lines)

if debug:
    print("Output text: " +str(lines)+"\n\n")
    
lines = lines.split(" ")

print("\nWord count: ", len(lines))

