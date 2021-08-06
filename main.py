from random import randint
from army_module import *
from character_module import *

import os
clear = lambda: os.system('cls')

armies = []

player_character = PlayerCharacter("Bolg the Usurper", "Warrior")
enemy_captain = Character()
player_army = Army(8000, 250, 1500, 5000, 2, 125, 5000, player_character)
enemy_army = Army(250, 10, 5, 100, 0, 0, 100, enemy_captain)
armies.append(player_army)
armies.append(enemy_army)

while True:
    clear()
    for i in range(0, len(armies)):
        print(f"{i}-army led by {armies[i].captain}")
    print("enter number to view army, enter unexisting number to exit:")
    army_number = int(input())
    clear()
    if army_number > len(armies)-1:
        print("See you again!")
        break
    else:
        while True:
            if armies[army_number].captain == 'Bolg the Usurper':
                print("0-end, 1-army report, 2-captain info")
                try:
                    command = int(input())
                except:
                    clear()
                    print("Don't input empty or invalid data!")
                else:
                    if command == 0:
                        clear()
                        break
                    elif command == 1:
                        clear()
                        armies[army_number].report()
                    elif command == 2:
                        clear()
                        armies[army_number].captain_info()
            else:
                print("0-end, 1-army report, 2-captain info, 3-gather intel")
                try:
                    command = int(input())
                except:
                    clear()
                    print("Don't input invalid or empty data!")
                else:
                    if command == 0:
                        clear()
                        break
                    elif command == 1:
                        clear()
                        armies[army_number].report()
                    elif command == 2:
                        clear()
                        armies[army_number].captain_info()
                    elif command == 3:
                        clear()
                        armies[army_number].intel_gathered = 1
                        armies[army_number].captain_info()