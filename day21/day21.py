from Parsers import parseBoss, parseStore
from Boss import Boss
from Player import Player
from Fighter import Fighter

def startGame(storeStr, bossStr):
    bossStats = parseBoss(bossStr)
    boss = Boss(*bossStats)
    store = parseStore(storeStr)
    minCost = -1
    # buy stuff
    for weapon in store.weapons:
        for armor in store.armors:
            for ring1 in store.rings:
                for ring2 in store.rings:
                    player = Player(weapon, armor, [ring1, ring2])
                    winner = battle(player, boss)
                    cost = weapon.cost + armor.cost + player.effectiveRing.cost
                    if (winner == Fighter.player):
                        if (cost < minCost or minCost == -1):
                            minLoadout = player
                            minCost = cost
                    bossStats = parseBoss(bossStr)
                    boss = Boss(*bossStats)
    print(minLoadout.printLoadout())
    return minCost

def battle(player, boss):
    while(player.hp > 0):
        #Player attack
        playerAttack = player.weapon.damage - boss.armor

        #Boss attack
        bossAttack = boss.damage - player.effectiveArmor

        #Resolve player attack
        if playerAttack >= 1:
            boss.hp = boss.hp - playerAttack
        else:
            boss.hp = boss.hp - 1

        #print("Player hits boss for {} damage, boss has {} hp remaining".format(playerAttack, boss.hp))
        
        if (boss.hp <= 0):
          break

        #Resolve boss attack
        if bossAttack >= 1:
            player.hp = player.hp - bossAttack
        else:
            player.hp = player.hp - 1

        #print("Boss hits Player for {} damage, Player has {} hp remaining".format(bossAttack, player.hp))

    # Resolve winner
    if (player.hp <= 0):
      return Fighter.boss
    else:
      return Fighter.player

bossStr = open(r'C:\Development\AdventOfCode\inputs\day21.txt').read()
storeStr = open(r'C:\Development\AdventOfCode\inputs\day21store.txt').read()
print(startGame(storeStr, bossStr))
