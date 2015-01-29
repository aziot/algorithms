#!/usr/bin/python

# ./runLength.py encode a b c a a b c a b b b c a b c c c c
# ./runLength.py encode a b c a a b c a b b b c a b c c c c c c c c c c 
# ./runLength.py encode a b c a a b c a b b b c a b c c c c c c c c c c a b c

# ./runLength.py decode a1b1c1a2b1c1a1b3c1a1b1c4
# ./runLength.py decode a1b1c1a2b1c1a1b3c1a1b1c4a10
# ./runLength.py decode a11b21c1a2b1c1a1b3c1a1b1c4
# ./runLength.py decode a11b21c1a2b1c1a1b3c1a1b1c4
# ./runLength.py decode a11b21c1a2b1c1a1b3c1a1b1c4c2

import sys

def consumeSingleCharacter(sequence):
  char2Encode = sequence[0]

  index = 0
  while index < len(sequence) and sequence[index] == char2Encode:
    index = index + 1

  return (char2Encode, index, sequence[index:])

def encode(sequence):
  if sequence:
    char, index, subsequence = consumeSingleCharacter(sequence)
    sys.stdout.write(str(index).join([char, '#']))
    encode(subsequence)

def isNumber(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def generateSingleCharacter(sequence):
  index = 1
  while index < len(sequence) and isNumber(sequence[index]):
    index = index + 1

  return (sequence[0], sequence[1:index], sequence[index+1:])
  
def decode(sequence):
  if sequence:
    char, count, subsequence = generateSingleCharacter(sequence)
    sys.stdout.write(char * int(count))
    decode(subsequence)
       
if len(sys.argv) <= 2:
  print 'Usage: runLength encode|decode <sequence>'
  sys.exit(1)

if sys.argv[1] == 'encode':
  encode(sys.argv[2])
  print
elif sys.argv[1] == 'decode':
  decode(sys.argv[2])
  print
