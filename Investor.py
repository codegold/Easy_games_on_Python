import random
import time

def displayIntro():
    print('''you are a skilled Investor''')
    print()


def chooseInvesting():
    instrument = '' #empty string
    while instrument != 'Business' and instrument != 'Stock':
        print('Which instrument you will invest?(press Business or Stock)')
        instrument = input()

    return instrument

def checkInstrument(chooseInvesting):
    print('You send your money...')
    time.sleep(2)
    print('make some trades...')
    time.sleep(2)
    print('Market opens and...')
    print()
    time.sleep(2)

    friendlyResult = random.randint(1,2)

    if chooseInvesting == str(friendlyResult):
        print('...You make 300% profit!')
    else:
        print('... You lose your invested money!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    checkInstrument = chooseInvesting()
    checkInstrument(caveNumber)


    print('Test your luck one more time? (yes or no)')
    playAgain = input()