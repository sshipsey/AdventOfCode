def callA(charA, charB, charC):
  print (charA + charB + charC)

a = {
  1: 'a',
  2: 'b',
  3: 'c'
} 
callA(*a.values())