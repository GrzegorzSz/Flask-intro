"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place
is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the
user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout
teh game and tell the user at the end.
"""
import random

tryesCount = 0


def generateNum():
    return random.randint(1000, 10000)


def compareNumbers(genNum, usrNum):
    result = {'win': False, 'cowsCount': 0, 'bullsCount': 0}
    passPositions = []
    if genNum == usrNum:
        result['win'] = True
    else:
        genNumStr = str(genNum)
        usrNumStr = str(usrNum)
        for pos in range(0, len(genNumStr)):  # looking for caws items
            if genNumStr[pos] == usrNumStr[pos]:
                passPositions.append(pos)
                result['cowsCount'] += 1
        genNumStr = list(genNumStr)
        usrNumStr = list(usrNumStr)
        for pos in passPositions:  # flag and remove items founding as cows
            genNumStr[pos] = ''
            usrNumStr[pos] = ''
        genNumStr = [item for item in genNumStr if item != '']
        usrNumStr = [item for item in usrNumStr if item != '']
        for item in usrNumStr:  # counting bulls
            if item in genNumStr:
                result['bullsCount'] += 1
    return result


generatedNum = generateNum()

while True:
    resp = input('Give 4-digit number: ')
    if resp.isnumeric() and len(resp) == 4:
        tryesCount += 1
        result = compareNumbers(generatedNum, int(resp))
        if result['win']:
            print('You won for %s try!\n' % tryesCount)
            generatedNum = generateNum()
        else:
            print('cows: {0}   bulls: {1}\n'.format(result['cowsCount'], result['bullsCount']))
    else:
        break
