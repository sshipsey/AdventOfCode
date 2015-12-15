from itertools import izip, permutations, tee
def day13(input):
  operatorLookup = {
  'gain' : '',
  'lose' : '-'
  }
  inputArr = [str.split() for str in input]
  peopleLookup = {tuple(sorted([stringArr[0], stringArr[-1][:-1]])) : eval(operatorLookup[stringArr[2]] + stringArr[3]) for stringArr in inputArr} 
  allPeople = list(set([str[0] for str in inputArr] + [str[-1][:-1] for str in inputArr]))

  allPerms = permutations(allPeople)
  maxHappiness = -1
  
  for arrangement in allPerms:
    thisArrangement = 0

    for i in range(0, len(arrangement) - 1):
      a,b = tee(arrangement)
      next(b, None)
      izip(a,b)
      thisArrangement = sum(peopleLookup[tuple(sorted([arrangement]))])
       
input = open(r'C:\Development\AdventOfCode\inputs\day13.txt').read().split('\n')
day13(input)