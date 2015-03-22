#!/usr/bin/python
import random, sys

days = 10
salary_bound = 10

salaries = [0] * days
for i in range(days):
  # salaries[i] = random.randint(-salary_bound, salary_bound)
  salaries[i] = random.randint(0, salary_bound)

print salaries

maxSalary = 0
maxSchedule = []

start = 0
while start < len(salaries):
  if salaries[start] > 0:  # this is the beginning of an interval
    end = start + 1
    while end < len(salaries) and salaries[end] > 0:
      end = end + 1
    end = end - 1

    even_sum = 0
    even_schedule = []
    index = start
    while index <= end:
      even_sum = even_sum + salaries[index]
      even_schedule.append(salaries[index])
      index = index + 2
    index = start
   
    odd_sum = 0 
    odd_schedule = []
    index = start + 1
    while index <= end:
      odd_sum = odd_sum + salaries[index]
      odd_schedule.append(salaries[index])
      index = index + 2

    if odd_sum < even_sum:
      maxSchedule.extend(even_schedule)
      maxSalary = maxSalary + even_sum
    else:
      maxSchedule.extend(odd_schedule)
      maxSalary = maxSalary + odd_sum
    start = end + 1

  else:
    start = start + 1
  

print maxSchedule, maxSalary    
