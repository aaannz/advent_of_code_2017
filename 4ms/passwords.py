#!/usr/bin/python3

# first task
def check_repeated_words(line):
  words = {}
  for word in line.strip().split():
    if words.get(word, False):
      return False
    words[word] = True
  return True 

# second task
def check_anagrams(line):
  words = {}
  for word in line.strip().split():
    word = ''.join(sorted(word))
    if words.get(word, False):
      return False
    words[word] = True
  return True

valid_lines = 0

with open('input.txt') as stream:
  for line in stream:
    if check_repeated_words(line) and check_anagrams(line):
      valid_lines += 1

print("Valid passphrases: {}".format(valid_lines))
