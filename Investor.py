import random
import time

def displayIntro():
    print('''You are a skilled Investor!''')
    print()


def chooseInvesting():
    instrument = '' #empty string
    while instrument != '1' and instrument != '2':
        print('Which instrument you will invest?(press 1 for Business or 2 for Stock)')
        instrument = input()

    return instrument

def checkInstrument(chooseInvesting):
    print('You send your money...')
    time.sleep(2)
    print('Make some trades...')
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
    checkNumber = chooseInvesting()
    checkInstrument(checkNumber)


    print('Test your luck one more time? (yes or no)')
    playAgain = input()