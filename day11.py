from itertools import groupby, tee, izip
def day11(password):
  password = toStr(int(password,36) + 1)
  
  while(not requirementsMet(password)):
    # Reset a to a and increment
    password = toStr(int(password,36) + 1)

  return password

def requirementsMet(passwordStr):
  
  # Cannot contain i, l, or o
  if any(badChar in passwordStr for badChar in ['i','l','o']):
    return False
  
  # Must contain 2 different pairs of non-overlapping letters
  if (sum([len(list(g)) / 2 for k, g in groupby(passwordStr, None)]) < 2):
    return False

  # Must contain one increasing straight line of letters
  a,b,c = tee(passwordStr, 3)
  next(b, None)
  next(c, None)
  next(c, None)

  if (not any([ord(x[0]) == ord(x[1]) - 1 == ord(x[2]) - 2 for x in izip(a,b,c)])):
    return False  

  # If we met all the requirements, return true
  return True 

def toStr(n):
   convertString = "a?????????abcdefghijklmnopqrstuvwxyz"
   if n < 36:
      return convertString[n]
   else:
      return toStr(n//36) + convertString[n%36]

input = "vzbxkghb"
firstPassword = day11(input)
print(day11(firstPassword))