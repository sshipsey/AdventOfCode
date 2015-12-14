def day7(input):
  operations = {
    "->" : '=',
    "AND" : "&",
    "OR" : "|",
    "LSHIFT" : "<<",
    "RSHIFT" : ">>",
    "NOT" : "~"
  }

  def isSolvable(token):
    if token in operations or token in solvedWires or token.isdigit():
      return True
    else:
      return False
  sequence = input.read().split('\n')
  circuitVals = {}
  solveStack = []
  solvedWires = []
  eqString = ""
  orderedSequence = sorted(sorted(sorted(sequence, key=lambda x: x if len(x.split()) is 3 else None), key=lambda x: len(x.split())), key=lambda x: -1 if x.split()[-1] is "a" else None)
  solveStack.insert(0, orderedSequence.pop(0))
  solveStack.insert(0, orderedSequence.pop(0))
  while len(orderedSequence) > 0 and len(solveStack) > 0:
    curEq = solveStack.pop(0).split()
    eqString = ""
    solvedWires.append(curEq[-1])  
    for idx, command in enumerate(orderedSequence):
      if all([isSolvable(token) for token in command.split()[0:-1]]):
        solveStack.insert(0, orderedSequence.pop(idx))
    for token in curEq[0:-2]:
      if token in operations:
        eqString += operations[token] 
      elif token in circuitVals:
        eqString += str(circuitVals[token])
      else:
        eqString += token
    circuitVals[curEq[-1]] = eval(eqString)

input = open(r'C:\Development\JS\inputs\day7.txt')
day7(input)