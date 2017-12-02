#!/bin/python3

import sys
import math

data = ""
try:
  with open(sys.argv[1]) as stream:
    for line in stream:
      data += line.strip()
except:
  data = input(">")

suma = 0
lastNum = int(data[0])
offset = len(data) / 2

print("Input: {}".format(data))
print("Len: {}, Offset {}".format(len(data), offset))

for i in range(0, len(data)):
  loffset = int((i + offset) % len(data))
  print("i {}, loffset {}".format(i, loffset))
  if data[i] == data[loffset]:
    suma += int(data[i])

#if data[0] == data[len(data)-1]:
#  suma += int(data[0])

print("Sum is {}".format(suma))
