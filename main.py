import random
from classes.mechanics import bcolors, Person
from classes.magic import Spell

# Spells
fire = Spell('Fireball', 10, 'attack', 100)
ice = Spell('Blizzard', 10, 'attack', 100)
lightning = Spell('Lightning', 12, 'attack', 150)

heal = Spell('Heal', 15, 'heal', 250)

# Characters
player = Person('Shadow', 500, 100, 50, 75, 35, [fire, ice, lightning, heal], [])
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

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(bcolors.RED + '\n' + enemy.name, 'strikes back for', str(enemy_damage), 'damage!' + bcolors.ENDC)

    if player.get_hp() is 0:
        print(bcolors.RED + '\nYou dead!', enemy.name, 'was victorious.' + bcolors.ENDC)
        is_fighting = False
    elif enemy.get_hp() is 0:
        print(bcolors.GREEN + '\nYou know he dead! You killed', enemy.name)
        is_fighting = False