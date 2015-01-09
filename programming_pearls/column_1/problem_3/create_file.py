#!/usr/bin/python

import random
import sys

if len(sys.argv) <= 1:
  print 'Usage: <max_integer> <num_ints_in_file>'
  sys.exit(1)

max_integer, num_ints_in_file = map(lambda x: int(x), sys.argv[1:])

f = open('out.pp', 'w')
random.seed()

selected_ints = range(1, max_integer + 1)
count_ints = max_integer
while count_ints:
  index = int(random.random() * count_ints)
  int_to_be_removed = selected_ints[index]
  if count_ints <= num_ints_in_file:
    f.write(str(int_to_be_removed) + '\n')
  count_ints = count_ints - 1
  selected_ints.remove(int_to_be_removed)

f.close()
