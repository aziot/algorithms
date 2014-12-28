#!/usr/bin/python

import sys

def symbolicMultiply(digit, multiplicant, offset):
  output = '0' * offset
  
  carry = 0
  for c in multiplicant[::-1]:
    newDigit = int(c) * digit + carry
    carry = 0
    if newDigit >= 10:
      carry = newDigit / 10
      newDigit = newDigit % 10
    output = str(newDigit) + output
 
  if carry > 0: 
    return str(carry) + output
  else:
    return output

def symbolicSum(a, b):
  maxLength = max(len(a), len(b))
  a = '0' * (maxLength - len(a)) + a
  b = '0' * (maxLength - len(b)) + b
  
  output = ''
  carry = 0
  for d1, d2 in zip(a[::-1], b[::-1]):
    newDigit = int(d1) + int(d2) + carry
    carry = 0
    if newDigit >= 10:
      carry = newDigit / 10
      newDigit = newDigit % 10
    output = str(newDigit) + output
    
  if carry > 0:
    print 'symbolic sum', a, b, str(carry) + output
    return str(carry) + output
  else:
    print 'symbolic sum', a, b, output
    return output

def sumPartialProducts(partialProducts):
  print 'sum partial products', partialProducts
  if not len(partialProducts):
    return ''
  elif len(partialProducts) == 1:
    return partialProducts[0]
  else:
    return symbolicSum(sumPartialProducts(partialProducts[2:]), symbolicSum(partialProducts[0], partialProducts[1]))

if len(sys.argv) < 3:
  print "Too few arguments. Usage: bigDecimalMultiplier <big int 1> <big int 2>"
  sys.exit(1)

bint1, bint2 = sys.argv[1:]

partialProducts = []

offset = 0
for c in bint1[::-1]:
  partialProducts.append([int(c), offset])
  offset = offset + 1

newPartialProducts = []
for p in partialProducts:
  digit, offset = p[0:2]
  newPartialProducts.append(symbolicMultiply(digit, bint2, offset))

print newPartialProducts
print sumPartialProducts(newPartialProducts)
