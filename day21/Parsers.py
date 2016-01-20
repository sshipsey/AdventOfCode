import re
from ItemType import ItemType
from Weapon import Weapon
from Armor import Armor
from Ring import Ring
from Store import Store
def parseBoss(bossStr):
    return [int(re.search("(?<=Hit Points: )\d+", bossStr).group(0)), \
    int(re.search("(?<=Damage: )\d+", bossStr).group(0)), \
    int(re.search("(?<=Armor: )\d+", bossStr).group(0))]

def parseStore(store):
    store = store.split('\n')
    itemType = None
    weapons = []
    armors = []
    rings = []
    weaponRgx = re.compile("Weapons:")
    armorRgx = re.compile("Armor:")
    ringRgx = re.compile("Rings:")
  
    for line in store:
        if (line == ""):
            continue
        if weaponRgx.match(line):
            itemType = ItemType.weapon
            continue
        if armorRgx.match(line):
            itemType = ItemType.armor
            continue
        if ringRgx.match(line):
            itemType = ItemType.ring
            continue
        if itemType == None:
            print("Error: Invalid item type read")
            break
    
        if (itemType == itemType.weapon):
            weapons.append(Weapon(*line.split()))
        elif (itemType == itemType.armor):
            armors.append(Armor(*line.split()))
        elif (itemType == itemType.ring):
            ringSpecs = re.findall("(\w+ \+\d).*?(\d+).*?(\d+).*?(\d+)", line)
            rings.append(Ring(*ringSpecs[0]))
    return Store(weapons, armors, rings)
