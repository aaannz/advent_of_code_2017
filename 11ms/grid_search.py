#!/usr/bin/python3

from sys import argv


'''
 Grid is hexagonal, using cube coordinates x,y,z as
   y
  /-\ x
  \-/
   z
'''
def step(direction, cur_pos):
  x = cur_pos[0]
  y = cur_pos[1]
  z = cur_pos[2]
  return {
    'n': (x,y+1,z-1),
    'ne': (x+1,y,z-1),
    'se': (x+1,y-1,z),
    's': (x,y-1,z+1),
    'sw': (x-1,y,z+1),
    'nw': (x-1,y+1,z)
  }[direction]

def follow_path(path, max_distance):
  cur_pos = (0,0,0)
  for i in path:
    cur_pos = step(i,cur_pos)
    d = distance(cur_pos)
    if d > max_distance:
      max_distance = d
  return cur_pos, max_distance

def distance(pos):
  return max(abs(pos[0]), abs(pos[1]), abs(pos[2]))

path = []
try:
  with open(argv[1]) as stream:
    path = stream.readline().strip().split(',')
except:
  path = input('>').strip().split(',')

child_pos, max_distance = follow_path(path, 0)
print("Child position is {}".format(child_pos))

# now get the shortest path by getting manhattan distance in cube
d = distance(child_pos)
print("Steps to reach child is {}".format(d))

#part2
print("Max distance child got is {}".format(max_distance))
