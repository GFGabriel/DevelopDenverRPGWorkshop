import random, math

class Spell:
    def __init__(self, name, cost, type, health_mod):
        self.name = name
        self.cost = cost
        self.type = type
        self.health_mod = health_mod

    def generate_spell_damage(self):
        spell_low = self.health_mod - math.floor(self.health_mod/20)
        spell_high = self.health_mod + math.floor(self.health_mod/20)
        return random.randrange(spell_low, spell_high)