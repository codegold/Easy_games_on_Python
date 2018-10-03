#tic tac toe game

import random

def drawBoard(board):
    # This Func returns board
    # Board has 10 str , 0 - ignored
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')

def inputPlayerLetter():
    # Allow player to input
    # Return list, where player's letter is 1st element, and computers is second.
    letter = ''
    while not (letter == 'X' or letter == '0'):
        print('You chose X or O?')
        letter = input().upper()

    # First element of the list is player's letter.
    if letter == 'X':
        return ['O', 'X']
    else:
        return ['X', 'O']

def whoGoesFirst():
    # Random first move select
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'You'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # True if player won
    # bo - means Board Le - means letter. For less inputting.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # over center
    (bo[1] == le and bo[2] == le and bo[3] == le) or  # over down
    (bo[7] == le and bo[4] == le and bo[1] == le) or  # over left
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down center
    (bo[9] == le and bo[6] == le and bo[3] == le) or # over right
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le) or # diagonal

def getBoardCopy(board):
    # Creates board copy and returns it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
        return boardCopy

def isSpaceFree(board, move):
    # Returns true if move in free cell.
    return board[move] == ' '

def getPlayerMove(board):
    # Allow player move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not in isSpaceFree(board, int(move)):
        print('Your next move? (1-9)')
        move = input()
    return  int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns next move considering moves already made.
    # Returns None if no allowed moves.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Considering board and computer's letter chose allowed move and return's it
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # This algorithm foi II TicTacToe
        # First check will we win doing next move.
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, computerLetter, i)
                if isWinner(boardCopy, computerLetter):
                    return i

    # Check whether player win if make next move and block it.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter):
            if isWinner(boardCopy, playerLetter):
                return i

    # Trying to busy one of corners, if there is free.
    move = choose


