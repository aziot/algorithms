#!/usr/bin/python

def update_frontier(row, column, frontier, component, row_length, column_width, matrix):
  """ Update the frontier with the neighbors of row, column) that are set in the matrix"""
  if column - 1 >= 0 and (row, column - 1) not in component and matrix[row][column - 1]:
    frontier.add((row, column - 1))
  if column + 1 < column_width and (row, column + 1) not in component and matrix[row][column + 1]:
    frontier.add((row, column + 1))
  if row - 1 >= 0 and (row - 1, column) not in component and matrix[row - 1][column]:
    frontier.add((row - 1, column))
  if row + 1 < row_length and (row + 1, column) not in component and matrix[row + 1][column]:
    frontier.add((row + 1, column))

# matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
matrix = [[0, 1, 1, 0], [1, 1, 1, 0]]

row_length = len(matrix)
column_width = len(matrix[0])

# each component is a list of elements that are part of the component.
# each element is a (row, column) pair.
# For example,
# 0 1 0 
# 1 1 0
# 0 0 0
# 1 0 0
# will be encoded as [[(0,1), (1, 0), (1, 1)], [(3, 0)]]
components = []

for row in range(row_length):
  for column in range(column_width):
    print 'examining', row, column
    if matrix[row][column] and not any([(row, column) in component for component in components]):
      # a new component starts here
      component = [(row, column)]
      print 'starting component', component
      frontier = set()
      update_frontier(row, column, frontier, component, row_length, column_width, matrix)
      print 'initial frontier', frontier

      while frontier:
        x, y = frontier.pop()
        component.append((x, y))
        update_frontier(x, y, frontier, component, row_length, column_width, matrix)

      components.append(component)

for component in components:
  print component
