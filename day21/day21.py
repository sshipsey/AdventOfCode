from Parsers import parseBoss, parseStore
from Boss import Boss
from Player import Player
from Fighter import Fighter

def startGame(storeStr, bossStr):

    # Initialize the boss and the store
    bossStats = parseBoss(bossStr)
    boss = Boss(*bossStats)
    store = parseStore(storeStr)
    minCost = -1
    
    # Buy stuff

    # test case
    # player = Player(store.weapons[2], store.armors[1], [store.rings[4]])
    # winner = battle(player, boss)
    # cost = player.weapon.cost + player.armor.cost + player.effectiveRing.cost
    # if (winner == Fighter.player):
    #     if (cost < minCost or minCost == -1):
    #         minLoadout = player
    #         minCost = cost

    # For all combinations of loadouts from the store
    for weapon in store.weapons:
        for armor in store.armors:
            for ring1 in store.rings:
                for ring2 in store.rings:

                    # cant use identical rings
                    if ring1.name == ring2.name and ring1.name != "":
                        continue
                    
                    # Create instance of player from store loadout
                    player = Player(weapon, armor, [ring1, ring2])
                    
                    # Declare winner from battle
                    winner = battle(player, boss)

                    # Calculate total cost
                    cost = weapon.cost + armor.cost + player.effectiveRing.cost
                    
                    # If the player won, and this is a new record, record it
                    # along with the player's loadout
                    if (winner == Fighter.player):
                        if (cost < minCost or minCost == -1):
                            minLoadout = player
                            minCost = cost

                    # Reset the boss for the next battle
                    bossStats = parseBoss(bossStr)
                    boss = Boss(*bossStats)

    # Return the winning loadout and its cost
    print(minLoadout.printLoadout())
    return minCost

def battle(player, boss):

    while(player.hp > 0):
        #Player attack
        playerAttack = player.weapon.damage + player.effectiveRing.damage - boss.armor

        #Boss attack
        bossAttack = boss.damage - player.effectiveArmor

        #Resolve player attack
        if playerAttack >= 1:
            boss.hp = boss.hp - playerAttack
        else:
            boss.hp = boss.hp - 1

        #print("Player hits boss for {} damage, boss has {} hp remaining".format(playerAttack, boss.hp))

        # If the player won on this turn, end the battle        
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
