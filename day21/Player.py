class Player:
    def __init__(self, weapon, armor, rings):
        self.weapon = weapon
        self.armor = armor
        self.rings = rings
        self.hp = 100
        w = weapon.armor if weapon.armor != None else 0
        a = armor.armor if armor.armor != None else 0
        r = sum([r.armor if r.armor != None else 0 for r in rings])
        self.effectiveArmor = w + a + r