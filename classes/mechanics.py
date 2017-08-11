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
    def __init__(self, name, hp, mp, atk, df, mpdf, magic, items, display_name):
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
        self.display_name = display_name

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

    def choose_item(self):
        i = 1
        print('Items:')
        for item in self.items:
            print('    '+str(i) + '.', item['item'].name + ':', item['item'].description, '(x' + str(item['quantity']) + ')')
            i += 1

    def replenish(self, mana):
        self.mp += mana
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def rejuvenate(self):
        self.hp = self.maxhp
        self.mp = self.maxmp

    def get_status(self):

        shown_hp = self.hp/self.maxhp * 100 / 4
        hp_bar = ''

        while shown_hp > 0:
            hp_bar += '█'
            shown_hp -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        hp_string = str(self.hp) + '/' + str(self.maxhp)
        current_hp = ''

        if len(hp_string) < 11:
            hp_space = 11 - len(hp_string)

            while hp_space > 0:
                current_hp += ' '
                hp_space -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string


        shown_mp = self.mp / self.maxmp * 100 / 5
        mp_bar = ''

        while shown_mp > 0:
            mp_bar += '█'
            shown_mp -= 1

        while len(mp_bar) < 20:
            mp_bar += ' '

        mp_string = str(self.mp) + '/' + str(self.maxmp)
        current_mp = ''

        if len(mp_string) < 9:
            mp_space = 9 - len(mp_string)

            while mp_space > 0:
                current_mp += ' '
                mp_space -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string



        print('                         _________________________            ____________________')

        print(bcolors.BOLD + self.name + '  ' + current_hp + '|' +
              bcolors.GREEN + hp_bar + bcolors.ENDC + '|' + bcolors.BOLD + ' ' + current_mp + '|' + bcolors.BLUE + mp_bar + bcolors.ENDC + '|')


    def get_enemy_status(self):
        hp_string = str(self.hp) + '/' + str(self.maxhp)
        current_hp = ''

        if len(hp_string) < 11:
            hp_spaces = 11 - len(hp_string)

            while hp_spaces > 0:
                current_hp += ' '
                hp_spaces -= 1

            current_hp += hp_string

        shown_hp = self.hp/self.maxhp * 100 / 4
        hp_bar = ''

        while shown_hp > 0:
            hp_bar += '█'
            shown_hp -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        mp_string = str(self.mp) + '/' + str(self.maxmp)
        current_mp = ''

        if len(mp_string) < 9:
            mp_spaces = 9 - len(mp_string)

            while mp_spaces > 0:
                current_mp += ' '
                mp_spaces -= 1

            current_mp += mp_string

        shown_mp = self.mp / self.maxmp * 100 / 5
        mp_bar = ''

        while shown_mp > 0:
            mp_bar += '█'
            shown_mp -= 1

        while len(mp_bar) < 20:
            mp_bar += ' '

        print('\n                         _________________________            ____________________')
        print(self.name + '  ' + current_hp + '|' + bcolors.RED + hp_bar + bcolors.ENDC + '|'  + ' ' + current_mp + '|' + bcolors.BLUE + mp_bar + bcolors.ENDC + '|' )
