#!/usr/bin/python3

from collections import deque

#genA = input('genA >')
#genB = input('genB >')

# test
#genA = 65
#genB = 8921
# expected result part1 588
# expected result part2 309

# task
genA = 679
genB = 771

fA = 16807
fB = 48271
divider = 2147483647

# part 1
#samples = 40000000

# part 2
samples = 5000000
dA = 4
dB = 8
qA = deque()
qB = deque()

matches = 0

def call_judge(qA, qB):
  a = qA.popleft() & 0b1111111111111111
  b = qB.popleft() & 0b1111111111111111
  return a == b

while samples > 0:
  nextA = (genA * fA) % divider
  nextB = (genB * fB) % divider
  genA = nextA
  genB = nextB

  if genA % dA == 0:
    qA.append(genA)
  if genB % dB == 0:
    qB.append(genB)

  if qA and qB:
    samples -= 1
    if call_judge(qA, qB):
      matches += 1

print("Matches after {} samples: {}".format(samples,matches))
