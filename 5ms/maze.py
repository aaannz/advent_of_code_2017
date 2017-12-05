#!/usr/bin/python3

import sys

def navigate_maze(maze):
  s = 0
  p = 0
  while(p < len(maze)):
#    print(maze)
    np = p + maze[p]
# 2np part contition
    if (maze[p] > 2):
      maze[p] -= 1
    else: 
      maze[p] += 1
    p = np
    s += 1
#  print(maze)
  return s

maze = []

with open(sys.argv[1]) as stream:
  for line in stream:
    maze.append(int(line.strip()))

steps = navigate_maze(maze)
print("To get out of maze we need {} steps.".format(steps))
