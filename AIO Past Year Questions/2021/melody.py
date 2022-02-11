#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Melody
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of notes.
N = None

# K is the largest number which could be a note.
K = None

# S contains the sequence of notes forming the song.
S = [None for x in range(100005)]

answer = None

# Open the input and output files.
input_file = open("melodyin.txt", "r")
output_file = open("melodyout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())

# Read each note in the song.
for i in range(0, N):
    S[i] = int(input_file.readline().strip())

# TODO: This is where you should compute your solution. Store the smallest
# possible number of notes Melody can change so that her song is nice into the
# variable answer.

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()