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
  for p in peopleLookup:
    print(p)  
  for arrangement in allPerms:
    thisArrangement = 0

    a,b = tee(arrangement)
    next(b, None)
    thisArrangement = sum([peopleLookup[tuple(sorted(x))] for x in izip(a,b)]) + peopleLookup[tuple(sorted([arrangement[0], arrangement[-1]]))]

    if thisArrangement > maxHappiness or maxHappiness == -1:
      maxHappiness = thisArrangement
  return maxHappiness 

input = open(r'C:\Development\AdventOfCode\inputs\day13.txt').read().split('\n')
print(day13(input))