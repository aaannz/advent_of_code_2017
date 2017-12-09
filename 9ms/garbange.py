#!/usr/bin/python3

from sys import argv

garbage_stream = ''

try:
  with open(argv[1]) as stream:
    garbage_stream = stream.readline()
except:
  garbage_stream = input('>')

glevel = 0
in_garbage = False
score = 0
ignore = False
garbage = 0

for c in garbage_stream:
#  print("C {} ignore {} group level {} garbage {}".format(c,ignore,glevel,in_garbage))
  if ignore:
    ignore = False
    continue
  if in_garbage:
    if c == ">":
      in_garbage = False
    elif c == "!":
      ignore = True
    else:
      garbage += 1
    continue

  if c == "{":
    glevel += 1
  elif c == "<":
    in_garbage = True
  elif c == "!":
    ignore = True
  elif c == "}":
    score += glevel
    glevel -= 1

print("Stream score is {}".format(score))
print("Garbage cleared {}".format(garbage))
