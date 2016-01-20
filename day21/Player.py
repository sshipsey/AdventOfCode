from Weapon import Weapon
from Armor import Armor
from Ring import Ring
class Player:
    def __init__(self, weapon = Weapon("", 0, 0, 0), armor = Armor("", 0, 0, 0), rings = []):
        self.weapon = weapon
        self.armor = armor
        self.rings = rings
        self.hp = 100
        w = weapon.armor if weapon.armor != None else 0
        a = armor.armor if armor.armor != None else 0
        r = sum([r.armor if r.armor != None else 0 for r in rings])
        self.effectiveArmor = w + a + r
        self.effectiveRing = self.combineRings()

    def combineRings(self):
        if len(self.rings) < 1:
          return Ring()
        if len(self.rings) < 2:
          return self.rings[0]
        else:
          return Ring("", self.rings[0].cost + self.rings[1].cost, self.rings[0].damage + self.rings[1].damage, self.rings[0].armor + self.rings[1].armor)