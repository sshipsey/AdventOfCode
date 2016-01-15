import re

def day19(input):
  molecule = input[-1]
  transformations = input[:-2]
  uniqueE = []
  for t in transformations:
    thisT = t.split(" ")[0]
    if thisT not in uniqueE:
      uniqueE.append(thisT)
  for x in uniqueE:
    print(x)
  molList = re.findall('[A-Z][^A-Z]*', molecule)
  print(molList)

input = open(r'C:\Development\AdventOfCode\inputs\day19.txt').read().split('\n')
print(day19(input))