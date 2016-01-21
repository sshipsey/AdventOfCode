import re
from ItemType import ItemType
from Weapon import Weapon
from Armor import Armor
from Ring import Ring
from Store import Store

# Parse text for boss data
def parseBoss(bossStr):
    return [int(re.search("(?<=Hit Points: )\d+", bossStr).group(0)), \
    int(re.search("(?<=Damage: )\d+", bossStr).group(0)), \
    int(re.search("(?<=Armor: )\d+", bossStr).group(0))]

# Parse text for store
def parseStore(store):
    store = store.split('\n')
    itemType = None
    weapons = []
    armors = []
    rings = []
    weaponRgx = re.compile("Weapons:")
    armorRgx = re.compile("Armor:")
    ringRgx = re.compile("Rings:")
  
    # For each item in the store (or header)
    for line in store:
        # Empty line
        if (line == ""):
            continue

        # Currently storing weapons
        if line.startswith(weaponRgx):
            itemType = ItemType.weapon
            continue

        # Currently storing armors
        if line.startswith(armorRgx):
            itemType = ItemType.armor
            continue

        # Currently storing rings
        if line.startswith(ringRgx):
            itemType = ItemType.ring
            continue

        # This should never happen
        if itemType == None:
            print("Error: Invalid item type read")
            break

        # Add to Weapons list
        if (itemType == itemType.weapon):
            weapons.append(Weapon(*line.split()))
        
        # Add to Armor list
        elif (itemType == itemType.armor):
            armors.append(Armor(*line.split()))
        
        # Add to Rings list
        elif (itemType == itemType.ring):
            ringSpecs = re.findall("(\w+ \+\d).*?(\d+).*?(\d+).*?(\d+)", line)
            rings.append(Ring(*ringSpecs[0]))

    # Append empty items as placeholder for non use
    armors.append(Armor())
    rings.append(Ring())

    # Create and return store instance with list of weapons, armors, and rings
    return Store(weapons, armors, rings)
