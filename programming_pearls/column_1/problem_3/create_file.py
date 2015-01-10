#!/usr/bin/python

import random
import sys

if len(sys.argv) <= 1:
  print 'Usage: <max_integer> <num_ints_in_file>'
  sys.exit(1)

max_integer, num_ints_in_file = map(lambda x: int(x), sys.argv[1:])

random.seed()

selected_ints = range(1, max_integer + 1)
res = set()
while len(res) < num_ints_in_file:
  index = int(random.random() * max_integer)
  int_chosen = selected_ints[index]
  if int_chosen not in res:
    res.add(int_chosen)

f = open('out.pp', 'w')
for i in res:
  f.write(str(i) + '\n')
f.close()
