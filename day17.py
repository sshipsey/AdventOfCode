import itertools
l = [y for x in [itertools.combinations([int(x) for x in list(open(r'C:\Development\AdventOfCode\inputs\day17.txt').read().split('\n'))], l) for l in range(len([int(x) for x in list(open(r'C:\Development\AdventOfCode\inputs\day17.txt').read().split('\n'))]))] for y in x if sum(list(y)) == 150]
minLen = 100
count = 0
for x in l:
  if len(x) < minLen:
    minLen = len(x)
for x in l:
  if len(x) == minLen:
    count += 1
print(count)