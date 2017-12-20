#!/usr/bin/python3

from sys import argv
from collections import deque
import re

def spin(count, positions):
  tmp = positions[:-count]
  del positions[:-count]
  positions.extend(tmp)

def exchange(posA, posB, positions):
  tmp = positions[posA]
  positions[posA] = positions[posB]
  positions[posB] = tmp

def partner(pA, pB, positions):
  posA, posB = None, None
  for n in range(len(positions)):
    if positions[n] == pA:
      posA = n
    elif positions[n] == pB:
      posB = n
    if posA and posB:
      break
  return exchange(posA, posB, positions)

# for test 5
positions = list(map(chr, range(ord('a'), ord('e')+1)))
# for real 16
#positions = list(map(chr, range(ord('a'), ord('p')+1)))
print(''.join(positions))

with open(argv[1]) as stream:
  for cmd in stream.readline().strip().split(','):
    if cmd[0] == 's':
      n = re.search(r's(\d+)', cmd).group(1)
      spin(int(n), positions)
    elif cmd[0] == 'x':
      n, m = sorted(map(int,re.search(r'x(\d+)/(\d+)', cmd).groups()))
      exchange(n, m, positions)
    elif cmd[0] == 'p':
      partner(cmd[1], cmd[3], positions)

# part 1
print("End sequence is {}".format(''.join(positions)))

# part 2
# get the final position mapping after all the dancing
mapping = list(range(len(positions)))
for n in range(len(positions)):
  l = ord('a') + n
  mapping[n] = positions.index(chr(l))
print(mapping)
dances = 1000000000 - 1
dances = 1
for i in range(dances):
  orgpos = positions.copy()
  for n in range(len(positions)):
    positions[mapping[n]] = orgpos[n]
print("End sequence is {}".format(''.join(positions)))
