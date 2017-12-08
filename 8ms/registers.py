#!/usr/bin/python3

from sys import argv
import re

def _check_register(r,registers):
  if registers.get(r) == None:
    registers[r] = 0

def more(r,v,registers):
  _check_register(r,registers)
  return registers[r] > v

def less(r,v,registers):
  _check_register(r,registers)
  return registers[r] < v

def eq(r,v,registers):
  _check_register(r,registers)
  return registers[r] == v

def more_or_eq(r,v,registers):
  _check_register(r,registers)
  return registers[r] >= v

def less_or_eq(r,v,registers):
  _check_register(r,registers)
  return registers[r] <= v

def not_eq(r,v,registers):
  _check_register(r,registers)
  return registers[r] != v

def eval_condition(r,v,op,registers):
  return {
    '>': more,
    '<': less,
    '==': eq,
    '>=': more_or_eq,
    '<=': less_or_eq,
    '!=': not_eq
  }[op](r,v,registers)

def inc(r,v,registers):
  _check_register(r,registers)
  registers[r] += v

def dec(r,v,registers):
  _check_register(r,registers)
  registers[r] -= v

def change_registers(r,v,op,registers):
  return {
    'inc': inc,
    'dec': dec
  }[op](r,v,registers)

def parse_instruction(line, registers, highest_value):
  reg, op, value, condition = re.search(r'(\w+) (dec|inc) ([-0-9]+) if (.*)', line).groups()
  cr, cop, cvalue = re.search(r'(\w+) ([<>=!]+) ([-0-9]+)', condition).groups()
  if eval_condition(cr,int(cvalue),cop,registers):
    change_registers(reg,int(value),op,registers)
    if registers[reg] > highest_value:
      return registers[reg]
  return highest_value

highest_value = 0
registers = {}
with open(argv[1]) as stream:
  for line in stream:
    highest_value = parse_instruction(line, registers, highest_value)

maxr = ''
maxv = 0
for r in registers:
  if registers[r] > maxv:
    maxv = registers[r]
    maxr = r

print("Maximum register is '{}' with value {}, highest value used {}".format(maxr, maxv, highest_value))
