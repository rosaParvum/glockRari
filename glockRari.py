#!/usr/bin/python
#
# ~~Brainfuck~~ glockRari Interpreter
# Copyright 2011 Sebastian Kaspari
# modified 2025 by rosaParvum
#

import sys
import getch
import re

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()


def evaluate(code):
  code     = re.findall(
      "my|in|glock|rari|Ra|Ri|I|gotta",
      code)
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]
    #print(command)

    if command == "my":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "in":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "glock":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "rari":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "Ra" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "Ri" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == "I":
        sys.stdout.write(chr(cells[cellptr]))
        #print("meow")

    if command == "gotta": cells[cellptr] = ord(getch.getch())
      
    codeptr += 1

def cleanup(code):
  return ''.join(filter(lambda x: x in ['I', 'gotta', 'Ra', 'Ri', 'in', 'my', 'glock', 'rari'], code))


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "Ra": temp_bracestack.append(position)
    if command == "Ri":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap


def main():
  if len(sys.argv) == 2: execute(sys.argv[1])
  else: print("Usage:", sys.argv[0], "filename")
  print("")

if __name__ == "__main__": main()

