#!/usr/bin/python

import operator
import sys

def digitOp(d1, d2, op, carry):
  newDigit = op(d1, d2) + carry
  carry = 0
  if newDigit >= 10:
    carry = newDigit / 10
    newDigit = newDigit % 10
  return newDigit, carry

def coreOp(n1, n2, op):
  """ n for number """
  output = ''
  carry = 0
  # d for digit
  for d1, d2 in zip(n1, n2):
    newDigit, carry = digitOp(int(d1), int(d2), op, carry)
    output = str(newDigit) + output
 
  if carry > 0: 
    return str(carry) + output
  else:
    return output

def symbolicMultiply(digit, multiplicant):
  return coreOp(multiplicant[::-1], [digit]*len(multiplicant), operator.mul)

def symbolicSum(a, b):
  maxLength = max(len(a), len(b))
  a = '0' * (maxLength - len(a)) + a
  b = '0' * (maxLength - len(b)) + b
  return coreOp(a[::-1], b[::-1], operator.add)

def sumPartialProducts(partialProducts):
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
for digit in bint1[::-1]:
  partialProducts.append(symbolicMultiply(int(digit), bint2 + '0' * offset))
  offset = offset + 1

print sumPartialProducts(partialProducts)
