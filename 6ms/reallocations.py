#!/usr/bin/python

import sys
banks = []
history = []

def relocate_banks(banks):
  m = max(banks)
  n = 0
  # find the bank to clear
  for i in range(len(banks)):
    if (banks[i] == m):
      n = i
      break
  
  todo = banks[n]
  banks[n] = 0
  # increment all banks starting with next to n(=n+1) and for todo times
  for i in range(n+1, todo+n+1):
#    print("Inc bank[{}]".format(i % len(banks)))
    banks[i % len(banks)] +=1
  
#  print(banks)
  return banks
       

with open(sys.argv[1]) as stream:
  banks = list(map(int, stream.readline().strip().split()))

step = 0
history.append(''.join(str(x) for x in banks))

done = False
cycle_start = 0
while not done:
  step += 1
  relocate_banks(banks)
  newhistory = ''.join(str(x) for x in banks)
  for i in range(len(history)):
    if newhistory == history[i]:
      cycle_start = i
      done = True
      break
  else:
    history.append(newhistory)

print("Inifinite loop detected at step {}".format(step))
print("Loop size is {}".format(step - cycle_start))
