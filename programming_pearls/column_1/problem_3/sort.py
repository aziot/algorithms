#!/usr/bin/env python

import sys

import BitVector

if len(sys.argv) <= 1:
  print 'Usage: <max_integer> <num_ints_in_file>'
  sys.exit(1)

max_integer, num_ints_in_file = map(lambda x: int(x), sys.argv[1:])

bv = BitVector.BitVector(size = max_integer)

# read the ints from the file

f = open('in.bv', 'r')
for i in f:
  bv[int(i)] = 1
f.close()

f = open('out.bv', 'w')
for index in xrange(len(bv)):
  if bv[index]:
    f.write(str(index) + '\n')
f.close()
