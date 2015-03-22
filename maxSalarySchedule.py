#!/usr/bin/python
import random, sys

def optimalSchedule(schedule):
  if not schedule:
    return 0, []
  elif len(schedule) == 1:  # include that day only if the salary is positive
    if schedule[0] > 0:
      return 1, schedule
    else:
      return 0, []
  else:
    subCost, subSchedule = optimalSchedule(schedule[1:])
    if schedule[0] <= 0:
      return subCost, subSchedule
    else:
      if schedule[1] != subSchedule[0]:
        return subCost + schedule[0], [schedule[0]] + subSchedule
      else:
        if schedule[0] > schedule[1]:
          return subCost + schedule[0] - schedule[1], [schedule[0]] + subSchedule[1:]
        else:
          return subCost, subSchedule

days = 10
salary_bound = 10

salaries = [0] * days
for i in range(days):
  # salaries[i] = random.randint(-salary_bound, salary_bound)
  salaries[i] = random.randint(0, salary_bound)
print salaries

print optimalSchedule(salaries)
