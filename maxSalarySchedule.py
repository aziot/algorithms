#!/usr/bin/python
import random, sys

def optimalSchedule(schedule):
  print schedule
  if not schedule:
    print 'return', 0, []
    return 0, []
  elif len(schedule) == 1:  # include that day only if the salary is positive
    if schedule[0] > 0:
      print 'return', schedule[0], schedule
      return schedule[0], schedule
    else:
      print 'return', 0, []
      return 0, []
  else:
    subCost, subSchedule = optimalSchedule(schedule[1:])
    if schedule[0] <= 0:
      print 'return', subCost, subSchedule
      return subCost, subSchedule
    else:
      if schedule[1] != subSchedule[0]:
        print 'return', subCost + schedule[0], [schedule[0]] + subSchedule
        return subCost + schedule[0], [schedule[0]] + subSchedule
      else:
        if schedule[0] > schedule[1]:
          subCost, subSchedule = optimalSchedule(schedule[2:])
          print 'return', schedule[0] + subCost, [schedule[0]] + subSchedule
          return schedule[0] + subCost, [schedule[0]] + subSchedule
        else:
          print 'return', subCost, subSchedule
          return subCost, subSchedule

days = 10
salary_bound = 10

salaries = [0] * days
for i in range(days):
  # salaries[i] = random.randint(-salary_bound, salary_bound)
  salaries[i] = random.randint(0, salary_bound)

# test input
# salaries = [7, 7, 2, 10, 9, 2, 1, 3, 5, 8]
print salaries
print optimalSchedule(salaries)
