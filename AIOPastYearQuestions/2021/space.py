#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)
 
#
# Solution Template for Space Mission
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#
 
# N is the number of available days.
N = None
 
# F is the amount of fuel available.
F = None
 
# C contains the fuel needed to open a portal on each day.
 
 
answer = None
 
# Open the input and output files.
input_file = open("spacein.txt", "r")
output_file = open("spaceout.txt", "w")
 
# Read the value of N and F.
input_line = input_file.readline().strip()
N, F = map(int, input_line.split())
 
# Read the cost to open a portal on each day.
C = []
for i in range(0, N):
    C.append(int(input_file.readline().strip()))
if len(C) <= 1:
    answer = -1
elif len(C) == 2:
    answer = 2 if C[0] + C[1] <= F else -1
else:
    I = sorted(range(len(C)), key=lambda k: C[k])
    L, R = [], []
    a, b = I.pop(0), I.pop(0)
    if C[a] + C[b] > F:
        answer = -1
    else:
        L.append(min(a, b)); R.append(max(a, b))
        while I:
            x = I.pop(0)
            if C[x] + min(C[L[-1]], C[R[-1]]) > F:
                break
            elif x < L[-1]:
                if C[x] + C[R[-1]] <= F:
                    L.append(x)
            elif x > R[-1]:
                if C[x] + C[L[-1]] <= F:
                    R.append(x)
    answer = R[-1] - L[-1] + 1
#print(answer)
# TODO: This is where you should compute your solution. Store the maximum
# number of samples you could collect into the variable answer.
# Write the answer to the output file.
output_file.write("%d\n" % (answer))
 
# Finally, close the input/output files.
input_file.close()
output_file.close()