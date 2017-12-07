#!/usr/bin/python3

import sys
import re

def find_root(tower):
  for proc in tower.keys():
    for p in tower:
      if proc in tower[p]['next']:
        break
    else:
      return proc

def assign_total_weight(tower, root):
  weight = tower[root]['weight']
  for p in tower[root]['next']:
    weight += assign_total_weight(tower, p)
  tower[root]['total_weight'] = weight
  return weight

def balance(tower, root):
  # get the proper tree weight
  w1 = 0
  w2 = 0
  w  = 0
  for p in tower[root]['next']:
    if tower[p]['total_weight'] == w1:
      w = w1
    elif tower[p]['total_weight'] == w2:
      w = w2
    else:
      if w1 == 0:
        w1 = tower[p]['total_weight']
      elif w2 == 0:
        w2 = tower[p]['total_weight']

  # get tree with wrong weight or return False if none is to be find
  culprit = ''
  for p in tower[root]['next']:
    if tower[p]['total_weight'] != w:
      culprit = p
      break
  else:
    return False, 0

  # go to next level
  w_proper, proc = balance(tower, culprit)
  if w_proper:
    return w_proper, proc
  else:
    return w, culprit

tower = {}

with open(sys.argv[1]) as stream:
  for line in stream:
    name, w, up = re.search(r"(\w+) \(([0-9]+)\)(?: -> )?(.*)", line).groups()
    ups = up.replace(' ','').split(',')
    if ups[0] == '':
      ups = []
    tower[name] = {
      'weight': int(w),
      'next': ups
    }

root = find_root(tower)
assign_total_weight(tower,root)
weight, culprit = balance(tower,root)
fixed_weight = 0
if weight > tower[culprit]['total_weight']:
  fixed_weight = tower[culprit]['weight'] + weight - tower[culprit]['total_weight']
else:
  fixed_weight = tower[culprit]['weight'] - tower[culprit]['total_weight'] + weight

print("root process is {}".format(root))
print("wrong process {} weight should be {}".format(culprit, fixed_weight))
