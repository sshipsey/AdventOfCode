import re
def day9(input, visited):
  if input[0][0] not in visited:
    print(visited)
    visited.append(input[0][0])
  thisLen = 0
  for trip in input:
    if trip[1] not in visited:
      visited.append(trip[1])
    thisLen += int(trip[2])
    inputCopy = input
    for trip in inputCopy:
      if trip[0] in visited or trip[1] in visited:
        inputCopy.remove(trip)
    if len(visited) >= 8:
      print(visited)
      return thisLen
    else:
      day9(inputCopy, visited)


input = open(r'C:\Development\AdventOfCode\inputs\day9.txt').read().split('\n')

inputArr = []
visited = []
for line in input:
  inputArr.append(re.split(' = | to ', line))
print(day9(inputArr, visited))