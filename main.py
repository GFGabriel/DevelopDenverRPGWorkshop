import random
from classes.mechanics import bcolors, Person

player = Person('Shadow', 500, 100, 50, 75, 35, [], [])
enemy = Person('Mr. World', 1500, 100, 40, 55, 55, [], [])

is_fighting = True

print(bcolors.BOLD + bcolors.RED + 'An enemy attacks!' + bcolors.ENDC)

while is_fighting:
    print ('\n' + player.name + ' is fighting ' + enemy.name + '.')

    print('\n' + player.name + ': HP ' + str(player.get_hp()) + '/' + str(player.get_maxhp()))
    print('\n' + enemy.name + ': HP ' + str(enemy.get_hp()) + '/' + str(enemy.get_maxhp()))


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

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(bcolors.RED + '\n' + enemy.name, 'strikes back for', str(enemy_damage), 'damage!' + bcolors.ENDC)

    if player.get_hp() is 0:
        print(bcolors.RED + '\nYou dead!', enemy.name, 'was victorious.' + bcolors.ENDC)
        is_fighting = False
    elif enemy.get_hp() is 0:
        print(bcolors.GREEN + '\nYou know he dead! You killed', enemy.name)
        is_fighting = False