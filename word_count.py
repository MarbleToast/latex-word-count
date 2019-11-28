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
    
    
def remove_latex(e, line, preserve_contents=False):
    change = False
    if debug:
        print("Looking for "+e+" in line "+line)

    if ("{" in e or "[" in e) and e in line and not preserve_contents:
        start = line.find(e)
        split_line = line[start:]
        end = split_line.find("}") + start
        if debug:
            print("Found "+e+" at char "+str(start)+" to "+str(end))
        line = line.replace(line[start:end+1], "")
        change = True
    elif e in line:
        if debug:
            print("Found "+e)
        line = line.replace(e, "")
        change = True
    return line, change


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
            '\\maketitle',
            '\\textsuperscript{',
            ]

PARTIAL_DEL_LIST = ['\\textsuperscript{',
                    '\\textit{',
                    '\\texttt{',
                    '\\',
                    '}']
    
lines = lines.splitlines()
for i in range(len(lines)):
    for e in DEL_LIST:
        if e in lines[i]:
            while e in lines[i]:
                lines[i] = remove_latex(e, lines[i])[0]
    for e in PARTIAL_DEL_LIST:
        if e in lines[i]:
            while e in lines[i]:
                lines[i] = remove_latex(e, lines[i], True)[0]



lines = list(filter(None, lines))

lines = " ".join(lines)

if debug:
    print("Output text: " +str(lines)+"\n\n")
    
lines = lines.split(" ")

print("\nWord count: ", len(lines))

