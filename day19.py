import re

def day19(input):
  molecule = input[-1]
  transformations = input[:-2]
  uniqueMolecules = []
  fromMol = []
  toMol = []
  counter = 0
  for idx, t in enumerate(transformations):
    thisT = t.split(" ")[0]
    transformT = t.split(" ")[2]
    fromMol.append(thisT)
    toMol.append(transformT)

  molList = re.findall('[A-Z][^A-Z]*', molecule)
  for j, c in enumerate(molList):
    for x, i in enumerate(fromMol):
      if i == c:
        tempVal = molList[:]
        tempVal[j] = toMol[x]
        tempMol = "".join(tempVal)
        if (tempMol not in uniqueMolecules):
          counter += 1
          uniqueMolecules.append(tempMol)

  return counter

input = open(r'C:\Development\AdventOfCode\inputs\day19.txt').read().split('\n')
print(day19(input))