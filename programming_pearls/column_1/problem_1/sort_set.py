#!/usr/bin/env python

import resource

res = set()
# read the ints from the file
f = open('in.bv', 'r')
for i in f:
  res.add(i)
f.close()

# write out the ints
f = open('out.bv', 'w')
for i in sorted(res):
  f.write(str(i) + '\n')
f.close()

print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
