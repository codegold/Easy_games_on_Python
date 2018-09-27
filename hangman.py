import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+ 
 0   |
 |   |
     |
    ===''', '''
 +---+
 0  |
/|  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
words = 'аист акула форель барсук верблюд воробей боров выдра гусь жаба зебра голубь \
         змея кобра индюк козел койот корова лебедь лосось лось лягушка медведь орел осел \
         панда паук питон попугай мышь норка пума семга скунс собака сова тигр собака кошка \
         утка ястреб стакан бутылка штанга гантеля гриф турник машина велосипед ролики охота \
         охота рыбалка спорт ресторан кафе пицца стейк салат десерт'.split()

def getRandomWord(wordList):
    #This function returns random str from list.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Mistaken letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #changes empties on guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Shows secret word with spaces between letters
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns letter, enterde by player. This func checks whether player entered one letter and nothing more.
    while True:
        print('Enter letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter just one letter.')
        elif guess in alreadyGuessed:
            print('You already entered this letter. Try another.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Please enter russian LETTER!')
        else:
            return guess

def playAgain():
    # This func returns True, if player wants to play again; other case returns False.
    print('Wanna play again? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #Allows to player enter word.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Checks whether player won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали! ')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Checks, whether player exceeded guess limit and lose.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You ran out of tries! \n Unrevealed letters: '+str(len(missedLetters))+' and revealed letters: \
                    '+str(len(correctLetters))+'. Secret word was"' +secretWord+ ' ".')
            gameIsDone = True

        # Ask whether player wanna play again (only of game finished).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord= getRandomWord(words)
        else:
            break


