import random
from classes.mechanics import bcolors, Person
from classes.magic import Spell
from classes.inventory import Item

#Items
potion = Item('Healing Potion', 'potion',
              'This mildly sweet potion heals a character for 50 health.', 50)
hi_potion = Item('Hi-Healing Potion', 'potion',
                 'This slightly bitter concoction heals a character for 100 health.', 100)
super_potion = Item('Super Potion', 'potion',
                    'The most bitter thing you will ever taste, but it heals for 500 health.', 500)

blue_drink = Item('Blue Drink', 'drink',
                  'Just as the name describes, this drink is quite blue. It replenishes 50 mana.', 50)

elixir = Item('Elixir', 'elixir',
              'This luminescent purple potion brings one person to full health and mana', 9999)

greek_fire = Item('Greek Fire', 'attack',
                  'This liquid is like lava in a bottle. When thrown it deals 500 fire damage', 500)

player_items = [{'item': potion, 'quantity': 15}, {'item': hi_potion, 'quantity': 5},
                {'item': super_potion, 'quantity': 5}, {'item': blue_drink, 'quantity': 15},
                {'item': elixir, 'quantity': 5}, {'item': greek_fire, 'quantity': 5}]

# Spells
fire = Spell('Fireball', 10, 'attack', 100)
ice = Spell('Blizzard', 10, 'attack', 100)
lightning = Spell('Lightning', 12, 'attack', 150)

heal = Spell('Heal', 15, 'heal', 250)

# Characters
player = Person('Shadow', 500, 100, 50, 75, 35, [fire, ice, lightning, heal], player_items)
enemy = Person('Mr. World', 1500, 100, 40, 55, 55, [], [])

is_fighting = True

print(bcolors.BOLD + bcolors.RED + 'An enemy attacks!' + bcolors.ENDC)

while is_fighting:
    print ('\n' + player.name + ' is fighting ' + enemy.name + '.')

    print('\n' + player.name + ': HP ' + str(player.get_hp()) + '/' + str(player.get_maxhp()) + ' MP ' +
          str(player.get_mp()) + '/' + str(player.get_maxmp()))
    print('\n' + enemy.name + ': HP ' + str(enemy.get_hp()) + '/' + str(enemy.get_maxhp()) + ' MP ' +
          str(enemy.get_mp()) + '/' + str(enemy.get_maxmp()))


    player.choose_action()
    choice = int(input('Choose an action: ')) - 1

    if choice is 0:
        is_crit = random.randrange(0, 10)
        if is_crit is 9:
            player_damage = player.generate_damage() * 3
            print(bcolors.YELLOW + '\nCritical hit!' + bcolors.ENDC, 'You strike the enemy for', str(player_damage), 'damage!')
            enemy.take_damage(player_damage)
        else:
            player_damage = player.generate_damage()
            print('\nYou strike the enemy for', str(player_damage), 'damage.')
            enemy.take_damage(player_damage)
    elif choice is 1:
        print('\nSpells:')
        player.choose_spell()
        spell_choice = player.magic[int(input('Choose a spell:')) - 1]
        spell_damage = spell_choice.generate_spell_damage()

        if spell_choice.cost > player.get_mp():
            print(bcolors.YELLOW + '\nYou do not have enough mana!' + bcolors.ENDC)
            continue

        player.reduce_mana(spell_choice.cost)

        if spell_choice.type is 'attack':
            spell_damage = spell_choice.generate_spell_damage()
            enemy.take_damage(spell_damage)
            print(bcolors.BLUE + '\nYou cast', spell_choice.name + '.', 'You deal', str(spell_damage), 'damage.')
        elif spell_choice.type is 'heal':
            player.heal(spell_choice.health_mod)
            print(bcolors.BLUE + '\nYou cast', spell_choice.name + '.', 'You heal', str(spell_damage), 'damage.')
    elif choice is 2:
        player.choose_item()
        item_choice = int(input('Choose your item:')) - 1
        item = player.items[item_choice]['item']

        if player.items[item_choice]['quantity'] is 0:
            print(bcolors.RED + '\nYou are out of', item.name + 's...' + bcolors.ENDC)
            continue

        player.items[item_choice]['quantity'] -= 1

        if item.type is 'potion':
            player.heal(item.prop)
            print(bcolors.BLUE + '\nYou use drink a', item.name + '.',
                  'You heal', item.prop, 'damage.' + bcolors.ENDC)
        elif item.type is 'attack':
            enemy.take_damage(item.prop)
            print(bcolors.YELLOW + '\nYou use', item.name + '.',
                  'Enemy takes', item.prop, 'damage.' + bcolors.ENDC)
        elif item.type is 'drink':
            player.replenish(item.prop)
            print(bcolors.BLUE + '\nYou use drink a', item.name + '.',
                  'You replenish', item.prop, 'mana.' + bcolors.ENDC)
        elif item.type is 'elixir':
            player.rejuvenate()
            print(bcolors.BLUE + '\nYou drink a', item.name + '.',
                  'Your mana and health have been completely restored.')
    else:
        print('Please choose a valid number')
        continue


    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(bcolors.RED + '\n' + enemy.name, 'strikes back for', str(enemy_damage), 'damage!' + bcolors.ENDC)

    if player.get_hp() is 0:
        print(bcolors.RED + '\nYou dead!', enemy.name, 'was victorious.' + bcolors.ENDC)
        is_fighting = False
    elif enemy.get_hp() is 0:
        print(bcolors.GREEN + '\nYou know he dead! You killed', enemy.name)
        is_fighting = False