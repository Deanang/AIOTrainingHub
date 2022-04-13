#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Social Distancing
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of meals.
N = None

# K is the minimum distance between hippos.
K = None

# D contains the locations of the meals.
D = [None for x in range(100005)]

answer = None

# Open the input and output files.
input_file = open("distin.txt", "r")
output_file = open("distout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())

# Read the locations of the meals.
D = [0] * N
for i in range(0, N):
    D[i] = int(input_file.readline().strip())
# TODO: This is where you should compute your solution. Store the maximum
# number of hippos that can be invited into the variable answer.
answer = 0
if N == 2:
    if abs(D[0] - D[1]) >= K:
        answer = 2
    else:
        answer = 1
elif K == 1:
    answer = len(set(D))
elif N == 1:
    answer = 1
else:
    answer = 1
    D = sorted(list(set(D)))
    current = D[0]
    for x in D[1:]:
        if x - current >= K:
            answer += 1
            current = x
# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()