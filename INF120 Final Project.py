import matplotlib.pyplot as plt
import numpy as np


def scoreMod(stat , modLis):
    group = 0
    if stat == 1:
        group = 1
    elif stat == 2 or stat == 3:
        group = 2
    elif stat == 4 or stat == 5:
        group = 3
    elif stat == 6 or stat == 7:
        group = 4
    elif stat == 8 or stat == 9:
        group = 5
    elif stat == 10 or stat == 11:
        group = 6
    elif stat == 12 or stat == 13:
        group = 7
    elif stat == 14 or stat == 15:
        group = 8
    elif stat == 16 or stat == 17:
        group = 9
    elif stat == 18 or stat == 19:
        group = 10
    elif stat == 20:
        group = 11
    mod = modLis[group - 1]
    return mod



if __name__ == '__main__':
    print("Welcome Adventurer! Let's build a character sheet!")
    print()

    name = input("Name:")
    race = input("Race:")
    clss = input("Class:")
    strength = int(input("Strength:"))
    dexterity = int(input("Dexterity:"))
    constitution = int(input("Constitution:"))
    intelligence = int(input("Intelligence:"))
    wisdom = int(input("Wisdom:"))
    charisma = int(input("Charisma:"))
    modLis = [-5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5]
    mod = 0

    print("Character Sheet: 5th Edition")
    print()
    print('Name:' + name + '  Race:' + race + '  Class:' + clss)
    print()
    print("Stat    Score    Modifier")

    stat = int()

    stat = strength
    mod = scoreMod(stat , modLis)
    print("STR     {:d}       {:d}".format(stat , mod))

    stat = dexterity
    mod = scoreMod(stat, modLis)
    print("DEX     {:d}       {:d}".format(stat , mod))

    stat = constitution
    mod = scoreMod(stat, modLis)
    print("CON     {:d}       {:d}".format(stat , mod))

    stat = intelligence
    mod = scoreMod(stat, modLis)
    print("INT     {:d}       {:d}".format(stat , mod))

    stat = wisdom
    mod = scoreMod(stat, modLis)
    print("WIS     {:d}       {:d}".format(stat , mod))

    stat = charisma
    mod = scoreMod(stat, modLis)
    print("CHA     {:d}       {:d}".format(stat , mod))

    statNames = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    statScores = [strength, dexterity, constitution, intelligence, wisdom, charisma]
    x = 0
    highest = 0
    index = 0
    while x < (len(statScores)-1):
        if statScores[x] > highest:
            highest = statScores[x]
            index = x
        x += 1
    highName = statNames[index]
    print('Your best ability is ' + highName + ' with a score of {:d}.'.format(highest))
    print()
    print("Good luck adventurer!")

    plt.bar(statNames, statScores)
    plt.title('Ability Scores')
    plt.xlabel('Ability')
    plt.ylabel('Score')
    plt.show()

    statRange= ['1', '2-3', '4-5', '6-7', '8-9', '10-11', '12-13', '14-15', '16-17', '18-19', '20']
    plt.bar(statRange, modLis)
    plt.title('Ability Modifiers')
    plt.xlabel('Ability Score')
    plt.ylabel('Modifier')
    plt.show()