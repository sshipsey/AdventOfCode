import re, itertools
def day9(input):
  allTowns = []
  distanceArr = []

  for line in input:
    expr = re.split(' = | to ', line)
    if (expr[0] not in allTowns):
      allTowns.append(expr[0])
    if (expr[1] not in allTowns):
      allTowns.append(expr[1])
    distanceArr.append(expr)

  allPerms = itertools.permutations(allTowns)
  minTrip = -1
  maxTrip = -1

  for trip in allPerms:
    thisTrip = 0
    
    for i in range(0, len(trip) - 1):
      for line in distanceArr:
        if trip[i] in line and trip[i+1] in line:
          thisTrip += int(line[2])
    
    if thisTrip < minTrip or minTrip is -1:
      minTrip = thisTrip
    if thisTrip > maxTrip or maxTrip is -1:
      maxTrip = thisTrip
  return {"min trip: " : minTrip, "max trip: " : maxTrip} 

input = open(r'C:\Development\AdventOfCode\inputs\day9.txt').read().split('\n')
print(day9(input))