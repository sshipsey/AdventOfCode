import re, operator
from itertools import chain, cycle, accumulate, islice

def day14(input):
    speeds = [re.findall("\d+", reindeer) for reindeer in input]
    reindeerMap = [cycle(chain([int(s[0])] * int(s[1]), [0] * int(s[2]))) for s in speeds]
    distances = [accumulate(r, operator.add) for r in reindeerMap]

    points = [0] * len(speeds)

    for i in range(0, 2503):
      d = [next(x) for x in distances]
      points = [p + 1 if d[idx] == max(d) else p for idx, p in enumerate(points)]
    return max(points)

input = open(r'C:\Development\AdventOfCode\inputs\day14.txt').read().split('\n')
print(day14(input))