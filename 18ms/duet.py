#!/usr/bin/python3

from sys import argv
from re import search
from collections import deque

def _getvalue(arg):
  val = None
  try:
    val = int(arg)
  except:
    val = registers.get(arg, 0)
  return val

def _checkreg(reg):
  if not registers.get(reg, False):
    registers[reg] = 0

def snd(arg, _x = None):
  val = _getvalue(arg)
  tgt = (curprg + 1) % 2
  queues[tgt].append(val)
  print(queues)
  if (curprg == 1):
    global counter
    counter += 1

def set(reg, arg):
  registers[reg] = _getvalue(arg)

def add(reg, arg):
  _checkreg(reg)
  registers[reg] += _getvalue(arg)

def mul(reg, arg):
  _checkreg(reg)
  registers[reg] *= _getvalue(arg)

def mod(reg, arg):
  _checkreg(reg)
  registers[reg] = registers[reg] % _getvalue(arg)

def rcv(reg, _x = None):
  if len(queues[curprg]) > 0:
    registers[reg] = queues[curprg].popleft()
    waiting[curprg] = False
  else:
    waiting[curprg] = True
    raise ValueError

def jgz(arg1, arg2):
  global ip
  val = _getvalue(arg1)
  if val > 0:
    ip += _getvalue(arg2)

def ctxSwitch(toprg):
  global registers, ip, curprg
  print("Context switch from {}, {}".format(registers, ip))
  if curprg != toprg:
    machines[curprg] = (registers, ip)
  registers, ip = machines[toprg]
  curprg = toprg
  print("Context switch to {}, {}".format(registers, ip))

def exe(i, args):
  reg= args[0]
  arg = args[1]
  return {
    'snd': snd,
    'set': set,
    'add': add,
    'mul': mul,
    'mod': mod,
    'rcv': rcv,
    'jgz': jgz
  }[i](reg, arg)

machines = [({'p': 0}, 0), ({'p': 1}, 0)]
curprg = 0
registers = None
program = list()
ip = 0
played = None
queues = [deque(), deque()]
waiting = [False, False]
counter = 0

with open(argv[1]) as stream:
  for line in stream:
    ins, reg, arg = search(r'([a-z]{3}) ([0-9a-z]) ?([-a-z0-9]*)$', line).groups()
    program.append({
      ins: [reg, arg]
    })

ctxSwitch(0)
prg_len = len(program)
while( ip < prg_len):
  try:
    _ip = ip
    i = list(program[ip].keys())[0]
#    print("{}: {} -> {}".format(ip, i, program[ip][i]))
    exe(i, (program[ip])[i])
    if ip == _ip:
      ip += 1
  except(ValueError):
    if waiting[0] and waiting[1] and len(queues[0]) == len(queues[1]) == 0:
      print(queues)
      print("Deadlock detected, exiting")
      print(machines)
      break
    else:
      ctxSwitch((curprg + 1) % 2)

print("Program 1 send {} values".format(counter))
