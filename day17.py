import itertools

# def day17(size, jars):
#   ways = [0] * (size + 1)
#   ways[0] = 1
#   for jar in jars:
#     for j in range(jar, size + 1):
#       ways[j] += ways[j - jar]
#   return ways[size]
def day17(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
        coins.remove(coin)
    return ways[amount]

jarSizes = list(sorted([int(jar) for jar in open(r'C:\Development\AdventOfCode\inputs\day17.txt').read().split("\n")]))
print(jarSizes)
print(day17(150, jarSizes))