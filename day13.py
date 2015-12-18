from itertools import izip, permutations, tee
def day13(input):
  
  operatorLookup = {
  'gain' : '',
  'lose' : '-'
  }
  
  inputArr = [str.split() for str in input]
  peopleLookup = {tuple([stringArr[0], stringArr[-1][:-1]]) : eval(operatorLookup[stringArr[2]] + stringArr[3]) for stringArr in inputArr} 
  allPeople = list(set([str[0] for str in inputArr] + [str[-1][:-1] for str in inputArr]))

  allPerms = permutations(allPeople)
  maxHappiness = -1

  for q in allPerms:
    thisArrangement = 0
    a,b = tee(q)
    next(b, None)
    z = izip(a,b)
    thisArrangement = sum([peopleLookup[x] + peopleLookup[tuple(reversed(x))] for x in z]) + sum([peopleLookup[tuple([q[0],q[-1]])], peopleLookup[tuple([q[-1],q[0]])]])

    if thisArrangement > maxHappiness or maxHappiness is -1:
      maxHappiness = thisArrangement

  return maxHappiness 

input = open(r'C:\Development\AdventOfCode\inputs\day13.txt').read().split('\n')
print(day13(input))