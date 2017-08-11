from classes.mechanics import bcolors, Person

player = Person('Shadow', 500, 100, 50, 75, 35, [], [])
enemy = Person('Mr. World', 1500, 100, 40, 55, 55, [], [])

is_fighting = True

print(bcolors.BOLD + bcolors.RED + 'An enemy attacks!' + bcolors.ENDC)

while is_fighting:
    print (player.name + ' is fighting ' + enemy.name + '.')
    is_fighting = False