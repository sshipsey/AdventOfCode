import re
from itertools import chain, cycle

def day14(input):
    speeds = [re.findall("(\d+)", reindeer) for reindeer in input]
    reindeerMap = [cycle(chain([int(s[0])] * int(s[1]), [0] * int(s[2]))) for s in speeds]
    maxDistance = max([sum([next(m, None) for x in xrange(0,2503)]) for m in reindeerMap])
    return maxDistance

input = open(r'C:\Development\AdventOfCode\inputs\day14.txt').read().split('\n')
print(day14(input))