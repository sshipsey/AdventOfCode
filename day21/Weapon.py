class Weapon:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = int(damage)
        self.armor = int(armor)