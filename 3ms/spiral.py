#!/bin/python3

target = 368078

spiral = {}

def count_value(x,y):
  ret = 0
  for dx, dy in [(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]:
    try:
      ret += spiral[x+dx,y+dy]
    except:
      pass
  return ret

spiral[0,0] = 1
spiral[1,0] = 1
x = 1
y = 1

while True:
  spiral[x,y] = count_value(x,y)
  if spiral[x,y] > target:
    break
  if spiral.get((x,y-1),0) != 0 and spiral.get((x-1,y),0) == 0:
    x -= 1
  elif spiral.get((x+1,y),0) != 0 and spiral.get((x,y-1),0) == 0:
    y -= 1
  elif spiral.get((x,y+1),0) != 0 and spiral.get((x+1,y),0) == 0:
    x += 1
  elif spiral.get((x-1,y),0) != 0 and spiral.get((x,y+1),0) == 0:
    y += 1

print("First value larger then {} is {}.".format(target, spiral[x,y]))
