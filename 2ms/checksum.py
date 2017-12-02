#!/bin/python3

import sys

lines = []
sums = []

def part_one(cols):
  max = int(cols[0])
  min = int(cols[0])
  for n in cols:
    n = int(n)
    if n < min:
      min = n
    elif n > max:
      max = n
  print("for {} max is {}, min is {}".format(cols,max,min))
  return max-min

def part_two(cols):
  for ni in range(len(cols) - 1):
    for mi in range(ni + 1, len(cols)):
      n = int(cols[ni])
      m = int(cols[mi])
      print("checking for n {} and m {}".format(n,m))
      if n % m == 0:
        return int(n/m)
      elif m % n == 0:
        return int(m/n)

with open(sys.argv[1]) as stream:
  for line in stream:
    cols = line.strip().split()
    sums.append(part_two(cols))

suma = 0
for n in sums:
  suma += n

print("sumas {}".format(sums))

print("Checksum is {}.".format(suma))
