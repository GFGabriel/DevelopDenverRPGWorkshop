import math

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