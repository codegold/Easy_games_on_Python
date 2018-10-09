import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # Returns str unique numbers, len of NUM_DIGITS.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ' '
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns str with hints 'Warm' 'Hot' and 'Cold'
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hot')
        elif guess[i] in secretNum:
            clues.append('Warm')
    if len(clues) == 0:
        return 'Cold'

    clues.sort()
    return ''.join(clues)

def isOnlyDigits(num):
    # Returns True, if num - str consisting just from numbers. Other case returns False
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('Я загадаю %s-x значное число, которое вы должны отгадать.' %(NUM_DIGITS))
print('Я дам несколько подсказок...')
print('Когда я говорю:    Это означает:')
print('   Cold            Ни одно цифра не отгадана.')
print('   Warm            Одна цифра отгадана, но не отгадана ее позиция.')
print('   Hot             Одна цифра и ее позиция отгаданы.')

while True:
    secretNum = getSecretNum()
    print('Итак, я загадала число. У вас есть %s попыток, чтобы отгадать его.' %(MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Try #%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken +=1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('Game over. It was %s.' % (secretNum))

    print('Wanna play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
