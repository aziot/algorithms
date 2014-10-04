#!/usr/bin/python

import sys

if __name__ == '__main__':
  text = sys.argv[1]
  pattern = sys.argv[2]

  n = len(pattern)
  m = len(text)

  if m < n:
    print 'text shorter than pattern'
    sys.exit()

  alignment_index = n - 1
  while alignment_index < m:
    print 'alignment_index', alignment_index
    pattern_index = n
    match_found = True
    while pattern_index > 0:
      pattern_index -= 1
      print 'pattern_index', pattern_index
      if pattern[pattern_index] != text[alignment_index - (n - 1) + pattern_index]:
        missmatch_char = text[alignment_index - (n - 1) + pattern_index]
        # find the missmatch char in the pattern
        missmatch_char_index = pattern.find(missmatch_char, 0, pattern_index + 1)
        if missmatch_char_index != -1:  # we found the missmatch char in the pattern
          alignment_index += (pattern_index - missmatch_char_index)
        else:
          alignment_index += (pattern_index + 1)
        match_found = False
        break
      if match_found:
        print 'match at ', alignment_index
        sys.exit()
  print 'no match'
