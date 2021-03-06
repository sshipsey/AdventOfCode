def day18(input):
    grid = [[True if l == '#' else False for l in x] for x in [list(x) for x in input]]

    gridCopy = [[False]*len(grid[0]) for _ in range(len(grid[0]))]
    for _ in range(100):
      for y, row in enumerate(grid):
        for x, node in enumerate(row):
          if ((x == 0 and y == 0) or (x == 0 and y == len(grid[0]) - 1) or (x == len(grid[0]) - 1 and y == 0) or (x == len(grid[0]) - 1 and y == len(grid[0]) - 1)):
            gridCopy[y][x] = True
          elif (grid[y][x]):
            if (countNeighbors(grid, y, x) in [2, 3]):
              gridCopy[y][x] = True
            else:
              gridCopy[y][x] = False
          else:
            if (countNeighbors(grid, y, x) == 3):
              gridCopy[y][x] = True
            else:
              gridCopy[y][x] = False

      grid = gridCopy.copy()
      gridCopy = [[False]*len(grid[0]) for _ in range(len(grid[0]))]

      #neighborsGrid = [countNeighbors(grid, y, x) for y, x in ]
      #print(neighborsGrid)
              
    return countLights(grid)
def countNeighbors(grid, y, x):
  count = 0
  l = len(grid[0]) - 1
  if y > 0 and grid[y-1][x]: count += 1
  if y > 0 and grid[y-1][x-1] and x > 0: count += 1
  if x < l and grid[y-1][x+1] and y > 0: count += 1

  if y < l and x < l and grid[y+1][x+1]: count += 1  
  if y < l and  grid[y+1][x-1]and x > 0: count += 1  
  if y < l and grid[y+1][x]: count += 1

  if x > 0 and grid[y][x-1]: count += 1
  if x < l and grid[y][x+1]: count += 1

  return count
def testGrid(grid):
  for row in grid:
      print("".join(["#" if x is True else "." for x in row]))


def countLights(grid):
  count = 0
  for q in grid:
    for z in q:
      if (z):
        count += 1
  return count
input = open(r'C:\Development\AdventOfCode\inputs\day18.txt').read().split('\n')
print(day18(input))