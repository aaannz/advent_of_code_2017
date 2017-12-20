#!/usr/bin/python3

from sys import argv
from re import match

network = list()

with open(argv[1]) as stream:
  for line in stream:
    network.append(list(line))

print(network)
# find the starting point
pos = (0,0)
direction = (0,0)
letters = str()
steps = 0

for i, c in enumerate(network[0]):
  if c == '|':
    pos = (0, i)
    direction = (1,0)
    break

print("pos: {}, dir: {}, letters: {}".format(pos, direction, letters))

def _tuplemath(a, b):
  return (a[0]+b[0], a[1]+b[1])

# follow the line
def follow():
  global pos, letters,steps
  while(network[pos[0]][pos[1]] != '+'):
    print("consumed {}".format(network[pos[0]][pos[1]]))
    if match(r'[a-zA-Z]', network[pos[0]][pos[1]]):
      letters += network[pos[0]][pos[1]]
    if network[pos[0]][pos[1]] == ' ':
      raise ValueError
    steps += 1
    pos = _tuplemath(pos, direction)
    print("moving to {}".format(pos))

def decide_direction():
  global direction, pos, steps
  directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
  for d in directions:
    # skip the one we just arrived
    if _tuplemath(d, direction) == (0,0):
      continue
    tmp = _tuplemath(pos, d)
    try:
      if network[tmp[0]][tmp[1]] != ' ':
        direction = d
        pos = tmp
        steps += 1
        break
    except:
      pass

try:
  while(True):
    follow()
    decide_direction()
except:
  print("Letters passed through: {}, steps taken {}".format(letters, steps))
