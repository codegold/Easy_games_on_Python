# Ceasar crypto
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS) # keeps max len of str

def getMode():
    while True:
        print('Do you wanna crypt or decrypt text?')
        mode = input().lower()
        if mode in ['crypt', 'c', 'decript', 'd']:
            return mode
        else:
            print('Enter "crypt" or "c" to cryption or "decrypt" or "d" for decryption.')

def getMessage():
    print('Enter text:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter crypto key (1-%s' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'p':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS.
            # Just add this symbol without changes.
            translated += symbol
        else:
            # encrypt or decrypt
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex >= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
        return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Transformed text:')
print(getTranslatedMessage(mode, message, key))


