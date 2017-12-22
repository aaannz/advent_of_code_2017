#!/usr/bin/python3

from sys import argv
from re import search

particles = list()

with open(argv[1]) as stream:
  for line in stream:
    # python re does not support capturing repeated groups, hence split in three
    # 0  1  2  3   4   5   6   7   8
    # x, y, z, vx, vy, vz, ax, ay, az
    p = search(r'p=< ?([-0-9]+),([-0-9]+),([-0-9]+)>', line.strip()).groups()
    v = search(r'v=< ?([-0-9]+),([-0-9]+),([-0-9]+)>', line.strip()).groups()
    a = search(r'a=< ?([-0-9]+),([-0-9]+),([-0-9]+)>', line.strip()).groups()
    par = list(map(int, list(p+v+a)))
    particles.append(par)

print("Loaded particles: {} ".format(len(particles)))
def distance(a,b,c):
  return abs(int(a))+abs(int(b))+abs(int(c))

# part 1
#mina = 99999
#minp = 0
#for n, p in enumerate(particles):
#  a = distance(p[6], p[7], p[8])
#  if a < mina:
#    mina = a
#    minp = n
#  elif a == mina:
#    print("Same a has p {}".format(n))
#
#print("mina {} for particle {}".format(mina, minp))
# part 2

# this is a cheat, just try 100 simulations, no way correct.
for i in range(100):
  positions = list()
  todelete = set()
  # update particle stats
  for n,p in enumerate(particles):
    p[3] += p[6]
    p[4] += p[7]
    p[5] += p[8]
    p[0] += p[3]
    p[1] += p[4]
    p[2] += p[5]

  # find colisions
    for pos in positions:
      if pos['pos'] == (p[0],p[1],p[2]):
#        print("p1: {}, p2: {}".format(pos['pos'], (p[0], p[1], p[2])))
        todelete.add(n)
        todelete.add(pos['par'])
        break
    else:
      positions.append({'pos':(p[0],p[1],p[2]),'par': n})

  todelete = sorted(list(todelete), reverse=True)
  for p in todelete:
    print("Particle {} collided".format(p))
    del particles[p]

print("Remaining particles: {}".format(len(particles))) 
