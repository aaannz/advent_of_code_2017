#!/usr/bin/python3

import sys

def reverse(p,l,data):
  n = 0
  size = len(data)
  while n < l - n:
    tmp = data[(p+n) % size]
    data[(p+n) % size] = data[(p+l-n) % size]
    data[(p+l-n) % size] = tmp
    n += 1

# copied and adapted from day 10
def knot_hash(data):
  lengths = list(map(ord, data))
  size = 256
  data = list(range(size))
  skip = 0
  pos = 0
  lengths += [17,31,73,47,23]
  for i in range(64):
    for l in lengths:
      reverse(pos,l-1,data)
      pos = (pos + l + skip) % size
      skip += 1

  dense_hash = list(range(16))
  for i in range(16):
    dense_hash[i] = data[i*16]
    for p in range(1+i*16,16+i*16):
      dense_hash[i] ^= data[p]
  return bytes(dense_hash).hex()

def hash2bin(h):
  ret = ''
  for c in h:
    ret += '{:004b}'.format(int(c,16))
  return ret

salt = input('>')

#part one counts used blocks
used_blocks = 0
#part two counts used regions
grid = list(range(128))
regions = 0

for i in range(128):
  line_usage = knot_hash('{}-{}'.format(salt,i))
  grid[i] = list(map(int, hash2bin(line_usage)))
  used_blocks += grid[i].count(1)
  for j in range(128):
    if grid[i][j] == 0:
      continue
    xreg, yreg = None, None
    if i > 0:
      xreg = grid[i-1][j]
    if j > 0:
      yreg = grid[i][j-1]
    reg = None
    if type(xreg) is list and type(yreg) is list and not xreg is yreg:
      for n,m in yreg:
        grid[n][m] = xreg
      xreg += yreg
      reg = xreg
      regions -= 1
    elif type(xreg) is list:
      reg = xreg
    elif type(yreg) is list:
      reg = yreg
    else:
      reg = list()
      regions += 1
    reg.append((i,j))
    grid[i][j] = reg

print("Used blocks {}".format(used_blocks))
print("Used regions {}".format(regions))
