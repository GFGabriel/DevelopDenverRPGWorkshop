from classes.mechanics import bcolors

is_fighting = True

print(bcolors.BOLD + bcolors.RED + 'An enemy attacks!' + bcolors.ENDC)

while is_fighting:
    print ('You are fighting')
    is_fighting = False