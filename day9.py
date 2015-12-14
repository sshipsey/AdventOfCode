import re
def day9(input):
  strInput = input.read().split('\n')
  inputArr = []
  allLocations = []
  traverseStack = []
  for line in strInput:
    expr = re.split(' = | to ', line)
    inputArr.append(expr)
    if (expr[0] not in allLocations):
      allLocations.append(expr[0])
    if (expr[1] not in allLocations):
      allLocations.append(expr[1])
  for a in inputArr:
    print(a)
  
  def dijkstra(graph, locations):
    Q = []
    dist = {}
    prev = {}
    for vertex in locations:
      dist[vertex] = None
      prev[vertex] = None
      Q.append(vertex)

    dist[locations[0]] = 0

    while len(Q) > 0:
      u = sorted(Q, key=lambda x: dist[x])[-1]
      Q.remove(u)
      neighbors = [l[0] for l in graph if l[1] == u] + [l[1] for l in graph if l[0] == u]
      print(u)
      print(neighbors)
      for neighbor in neighbors:
        for info in graph:
          if (info[0] == u or info[1] == u) and (info[0] == neighbor or info[1] == neighbor):
            neighborDist = info[-1]
        print(neighborDist)
        alt = dist[u] + int(neighborDist)
        if alt < dist[neighbor]:
          dist[neighbor] = alt
          prev[v] = u
    return {"dist" : dist,"prev" : prev}

  print(dijkstra(inputArr, allLocations))

input = open(r'C:\Development\AdventOfCode\inputs\day9.txt')
day9(input)