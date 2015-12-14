def day10(input):
  c = 1
  output = ""
  
  for _ in range(0, 50):
    for i in range(0, len(input) - 1):
      if input[i] is not input[i + 1]:
        output += str(c) + input[i]
        c = 1
      else:
        c += 1
    output += str(c) + input[len(input) - 1]
    input = output
    output = ""
    c = 1
  return len(input)

input = "1321131112"
print(day10(list(input)))