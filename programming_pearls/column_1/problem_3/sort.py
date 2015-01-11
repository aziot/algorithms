#!/usr/bin/env python

import resource
import sys

import BitVector

if len(sys.argv) <= 1:
  print 'Usage: <max_integer>'
  sys.exit(1)

max_integer = int(sys.argv[-1])

bv = BitVector.BitVector(size = max_integer)

# read the ints from the file
f = open('in.bv', 'r')
for i in f:
  bv[int(i)] = 1
f.close()

# write out the ints
f = open('out.bv', 'w')
for index in xrange(len(bv)):
  if bv[index]:
    f.write(str(index) + '\n')
f.close()

print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
