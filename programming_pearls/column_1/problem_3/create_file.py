#!/usr/bin/python

import random
import sys

if len(sys.argv) <= 1:
  print 'Usage: <max integer> <num_ints_in_file>'
  sys.exit(1)

max_integer, num_ints_in_file = map(lambda x: int(x), sys.argv[1:])

int_density = num_ints_in_file / float(max_integer)

count_ints = 0
random.seed()
already_added = []

f = open('out.pp', 'w')
while count_ints < num_ints_in_file:
  for i in xrange(1, max_integer+1):  # the int to be added will never exceed max_integer
    if random.random() > int_density and count_ints < num_ints_in_file and i not in already_added:  # we get a uniform distribution of ints
      count_ints = count_ints + 1
      already_added.append(i)
      f.write(str(i) + '\n')

f.close()
