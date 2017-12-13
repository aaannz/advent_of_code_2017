#!/usr/bin/python3

from sys import argv

def move_scanners(firewall):
  for n, l in firewall.items():
    if l['scan'] == l['range'] - 1:
      l['scanup'] = True
    elif l['scan'] == 0:
      l['scanup'] = False

    if l['scanup']:
      l['scan'] -= 1
    else:
      l['scan'] += 1

def reset_firewall(firewall):
  for n, l in firewall.items():
    l['scanup'] = False
    l['scan'] = 0

def step_firewall(pos, firewall, caught_is_fatal):
  caught = False
  if firewall.get(pos):
    if firewall[pos]['scan'] == 0:
      caught = True
  
  move_scanners(firewall)

  if caught:
    if caught_is_fatal:
      raise
    return pos * firewall[pos]['range']
  else:
    return 0

def do_firewall(firewall, caught_is_fatal=False):
  severity = 0
  for i in range(max(firewall) + 1):
    severity += step_firewall(i, firewall, caught_is_fatal)
  return severity

firewall = {}
with open(argv[1]) as stream:
  for line in stream:
    d, r = map(int, line.strip().split(':'))
    firewall[d] = {
      'range': r,
      'scan': 0,
      'scanup': False,
    }

# part 1
print("Passed firewall with severity {}".format(do_firewall(firewall)))

# part2 - flood the firewall with packets, delete them as they are being caught. The one that makes it through
# its packet number is the delay
reset_firewall(firewall)
delay = 0
winner = 0
packets = {}
while (winner == 0):
  packets[delay] = {
    'pos': 0,
  }
  for n in list(packets.keys()):
    p = packets[n]
    # iterate over not guarded layers
    if not firewall.get(p['pos']):
      p['pos'] += 1
      continue
    # eliminate if caught
    if firewall[p['pos']]['scan'] == 0:
      del packets[n]
      continue
    else:
      p['pos'] += 1

    # if packet position is after last scanner, we won
    if p['pos'] > max(firewall):
      winner = n
      break
  delay += 1
  move_scanners(firewall)
print("Passed firewall without being caught by delaying entry {} ps".format(winner))
