"""
Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program
that the player has to guess, letter by letter. The player guesses one letter at a time until
the entire word has been guessed. (In the actual game, the player can only guess 6 letters
incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write
the logic that asks a player to guess a letter and displays letters in the clue word
that were guessed correctly. For now, let the player guess an infinite number
of times until they get the entire word. As a bonus, keep track of the letters
the player guessed and display a different message if the player tries to guess
that letter again. Remember to stop the game when all the letters have been guessed
correctly! Don’t worry about choosing a word randomly or keeping track of the number
of guesses the player has remaining - we will deal with those in a future exercise.
"""

from pickWord import pickWord


def seekTheLetterInWord(userLetters, wordL, letter):
    letterInWord = False
    if letter in wordL:
        userLetters.add(letter)
        letterInWord = True
    return letterInWord


def showLetterInWord(gWord, uLetters, wordL):
    for count in range(len(wordL)):
        if gWord[count] == '_':
            if wordL[count] in uLetters:
                gWord[count] = wordL[count]


def printWordFromList(word):
    for letter in word:
        print(letter, end='')
    print()


def guessTheWord():
    attemptscounter = 6
    wordList = list(pickWord())
    userLetters = set()
    userGivenLetters = set()
    guessWord = []
    print('Welcome to Hangman!')
    for _ in wordList:
        print('_', end='')
        guessWord.append('_')
    print()
    while '_' in guessWord:
        inp = input('Give a letter: ').upper()
        if seekTheLetterInWord(userLetters, wordList, inp):
            userGivenLetters.add(inp)
            showLetterInWord(guessWord, userLetters, wordList)
        else:
            if inp not in userGivenLetters:
                attemptscounter -= 1
            userGivenLetters.add(inp)
            print('Incorrect!')
        printWordFromList(guessWord)
        if attemptscounter < 1: break
        print('attempts left:', attemptscounter)

    if attemptscounter < 1:
        print('You lose.\nThe word is', printWordFromList(wordList))
    else:
        print('Congratulations')


if __name__ == '__main__':
    again = True
    while again:
        guessTheWord()
        if input('Play again? (y/n): ').lower() == 'n':
            again = False
