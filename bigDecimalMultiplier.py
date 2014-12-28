#!/usr/bin/python

import operator
import sys

def digitOp(d1, d2, op, carry):
  """ building block for combining digits d1 and d2 with op and taking the carry into consideration"""
  newDigit = op(d1, d2) + carry
  carry = 0
  if newDigit >= 10:
    carry = newDigit / 10
    newDigit = newDigit % 10
  return newDigit, carry

def rippleOp(n1, n2, op):
  """ combine numbers n1 and n2 digit by digit using op """
  output = ''
  carry = 0
  # d for digit
  # ripple starts from the lowest digit
  for d1, d2 in zip(n1[::-1], n2[::-1]):
    newDigit, carry = digitOp(int(d1), int(d2), op, carry)
    output = str(newDigit) + output
 
  if carry > 0: 
    return str(carry) + output
  else:
    return output

def symbolicMultiply(digit, multiplicant):
  return rippleOp(multiplicant, [digit]*len(multiplicant), operator.mul)

def symbolicSum(n1, n2):
  """ n for number """
  maxLength = max(len(n1), len(n2))
  n1 = '0' * (maxLength - len(n1)) + n1
  n2 = '0' * (maxLength - len(n2)) + n2
  return rippleOp(n1, n2, operator.add)

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

# multiply each digit of bint1 with a shifted version of bint2 starting from the lowest digit
# store each partial product in a list
partialProducts = []
offset = 0
for digit in bint1[::-1]:
  partialProducts.append(symbolicMultiply(int(digit), bint2 + '0' * offset))
  offset = offset + 1

# sum the partial products
print sumPartialProducts(partialProducts)
