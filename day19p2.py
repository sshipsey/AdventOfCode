from random import shuffle

input = open(r'C:\Development\AdventOfCode\inputs\day19.txt').read().split('\n')
reps = [tuple([x.split(" ")[0], x.split(" ")[2]]) for x in input[:-2]]

mol = input[-1]
target = mol
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = mol
        part2 = 0
        shuffle(reps)

print part2

