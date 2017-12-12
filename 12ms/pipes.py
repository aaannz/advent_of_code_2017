#!/usr/bin/python3

from sys import argv
from re import search

def gather_group(pid, conns):
  if conns[pid]['done']:
    return []
  ret = [pid]
  conns[pid]['done'] = True
  for p in conns[pid]['cons']:
    ret += gather_group(p, conns)

  return ret

connections = {}

with open(argv[1]) as stream:
  for line in stream:
    pid, conns = search(r'(\d+) <-> (.*)', line.strip()).groups()
    con = list(map(int,conns.split(',')))
    connections[int(pid)] = {
      'cons': con,
      'done': False
    }

start = 0
pgroup = []

pgroup = gather_group(start, connections)
print("Pid {} group contains {} programs".format(start, len(pgroup)))

groups = [pgroup]

for p in connections:
  g = gather_group(p, connections)
  if g:
    groups.append(g)

print("Total number of groups is {}".format(len(groups)))
