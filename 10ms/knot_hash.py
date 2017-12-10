#!/usr/bin/python3

from sys import argv

def reverse(p,l,data):
  n = 0
  while n < l - n:
    tmp = data[(p+n) % size]
    data[(p+n) % size] = data[(p+l-n) % size]
    data[(p+l-n) % size] = tmp
    n += 1

lengths = []

try:
  with open(argv[1]) as stream:
    # part1
    #lengths = map(int, stream.readline().split(','))
    # part2
    lengths = list(map(ord, stream.readline().strip()))
except:
  lengths = list(map(ord, input('>')))

# 5 for test, 255 for run
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

# part 1 - only 1 loop
#print("Checksum is {}".format(data[0] * data[1]))

dense_hash = list(range(16))
for i in range(16):
  dense_hash[i] = data[i*16]
  for p in range(1+i*16,16+i*16):
    dense_hash[i] ^= data[p]

print(bytes(dense_hash).hex())
