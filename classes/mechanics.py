import math, random

# https://godoc.org/github.com/whitedevops/colors

class bcolors:
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, mpdf, magic, items):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - math.floor(atk/10)
        self.atkh = atk + math.floor(atk/10)
        self.df = df
        self.mpdf = mpdf
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def choose_action(self):
        i = 1
        print('\nActions:')
        for item in self.actions:
            print('    '+str(i)+'.', item)
            i += 1

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, health_mod):
        self.hp += health_mod
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def reduce_mana(self, cost):
        self.mp -= cost

    def choose_spell(self):
        i = 1
        for spell in self.magic:
            print('    ' + str(i) + '.', spell.name, '  (cost:', str(spell.cost) + ')')
            i += 1