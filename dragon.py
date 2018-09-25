import random
import time

def displayIntro():
    print('''you are in Dragon land. 
    In front of you two caves. In one of them - kind dragon, who will gift you with 
    treasures. But in second - another dragon who want kill you!''')
    print()


def chooseCave():
    cave = '' #empty string
    while cave != '1' and cave != '2':
        print('Which cave you will enter?(press button 1 or 2)')
        cave = input()

    return cave

def checkCave(chooseCave):
    print('You approaching to cave...')
    time.sleep(2)
    print('Its darkness makes you trmble with fear...')
    time.sleep(2)
    print('The big dragon jumps out in front of you! He reveals his mouth and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chooseCave == str(friendlyCave):
        print('...shares his treasures with you!')
    else:
        print('... instantly eat you!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)


    print('Test your luck one more time? (yes or no)')
    playAgain = input()