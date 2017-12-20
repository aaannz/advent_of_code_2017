#!/usr/bin/python3

from collections import deque
steps = int(input('>'))

buf = [0]
pos = 0
# part 1
#finish = 2018
# part 2
finish = 50000000
buflen = 1
val = None

for i in range(1,finish):
  pos = ((pos + steps) % buflen) + 1
  if pos == 1:
    val = i
  buflen += 1
#  buf = buf[:pos] + [i] + buf[pos:]

# part 1
#print(buf[(pos+1) % len(buf)])
# part 2
print(val)
