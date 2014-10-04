#!/usr/bin/python

import sys

def create_backtracking_table(pattern):
  T = {};
  T[0] = -1;
  for i in range(1, len(pattern)):
    T[i] = 0;
  for i in range(1, len(pattern)):
    print 'offseat',i
    for j in range(1, len(pattern) - i):
      if pattern.startswith(pattern[i : i + j]):
        T[i + j] = j
        print 'second offset', j, ' ', pattern[i : i + j], ' prefix of ', pattern
        print T
      
  return T;

if __name__ == '__main__':
  pattern = sys.argv[1]  # what we are looking for
  text = sys.argv[2]  # 'pattern' should be in here

  print 'pattern', pattern
  print 'text', text

  # prepare the backtrack dictionary
  T = create_backtracking_table(pattern);

  print 'The backtracking dictionary,', T
 
  m = 0 # offset inside the text
  while m < len(text):
    print 'm == ', m
    success = True;
    i = 0;
    while i < len(pattern):
      print 'i == ', i
      if m + i >= len(text):
        print 'no match!';
        sys.exit();
         
      if text[m + i] != pattern[i]:
        m = m + i - T[i]
        success = False;
        break;
      i = i + 1;
    if success:
      print 'match', m;
      break;

  if not success:
    print 'no match!';
