import re

def isValidCombination(a,b,c,d):
  return True if a + b + c + d == 100 else False

def day15(input):
    maxValue = -1

    # Create ingredient lookup dictionary
    regex = r'(\w+): (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+)'
    ingredientLookup = {key: {
        cap: int(capNum),
        dur: int(durNum),
        flv: int(flvNum),
        tex: int(texNum),
        cal: int(calNum)} for key, cap, capNum, dur, durNum, flv, flvNum, tex, texNum, cal, calNum in re.findall(regex, input) \
        for key, cap, capNum, dur, durNum, flv, flvNum, tex, texNum, cal, calNum in re.findall(regex, input)}

    # Partition
    validCombinations = [[a,b,c,100-a-b-c] for a in range(100) for b in range(100 - a) for c in range(100 - a - b) if isValidCombination(a,b,c,100 - a - b - c)]
    
    for combination in validCombinations:
      total = score(combination, ingredientLookup)
      if total > maxValue or maxValue == -1:
        maxValue = total

    return maxValue

# Get the score of this partition
def score(inp, ingredientLookup):

  sugarCount, sprinklesCount, candyCount, chocolateCount = inp

  cap = ingredientLookup["Sugar"]["capacity"] * sugarCount \
  + ingredientLookup["Candy"]["capacity"] * candyCount \
  + ingredientLookup["Chocolate"]["capacity"] * chocolateCount \
  + ingredientLookup["Sprinkles"]["capacity"] * sprinklesCount

  if cap < 0:
    cap = 0

  tex = ingredientLookup["Sugar"]["texture"] * sugarCount \
  + ingredientLookup["Candy"]["texture"] * candyCount \
  + ingredientLookup["Chocolate"]["texture"] * chocolateCount \
  + ingredientLookup["Sprinkles"]["texture"] * sprinklesCount

  if tex < 0:
    tex = 0

  dur =  ingredientLookup["Sugar"]["durability"] * sugarCount \
  + ingredientLookup["Candy"]["durability"] * candyCount \
  + ingredientLookup["Chocolate"]["durability"] * chocolateCount \
  + ingredientLookup["Sprinkles"]["durability"] * sprinklesCount

  if dur < 0:
    dur = 0

  flv = ingredientLookup["Sugar"]["flavor"] * sugarCount \
  + ingredientLookup["Candy"]["flavor"] * candyCount \
  + ingredientLookup["Chocolate"]["flavor"] * chocolateCount \
  + ingredientLookup["Sprinkles"]["flavor"] * sprinklesCount

  if flv < 0:
    flv = 0

  cal = ingredientLookup["Sugar"]["calories"] * sugarCount \
  + ingredientLookup["Candy"]["calories"] * candyCount \
  + ingredientLookup["Chocolate"]["calories"] * chocolateCount \
  + ingredientLookup["Sprinkles"]["calories"] * sprinklesCount

  if cal == 500:
    return cap * tex * dur * flv
  else:
    return 0

input = open(r'C:\Development\AdventOfCode\inputs\day15.txt').read()
print(day15(input))