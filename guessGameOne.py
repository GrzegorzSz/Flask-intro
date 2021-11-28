"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random


def chooseNewNum():
    print('\nGuess the number (1-10)')
    return random.randint(1, 10)


def play():
    rnumber = chooseNewNum()
    tryes = 0
    while True:
        playerReply = input('Your number (exit to quit):')
        if playerReply == 'exit' or playerReply == 'quit':
            break

        tryes += 1
        if rnumber == int(playerReply):
            print('CONGRATULATIONS you have guessed for %s time' % tryes)
            rnumber = chooseNewNum()
            tryes = 0
        else:
            if int(playerReply) < rnumber:
                print('The number is higher')
            else:
                print('The number is lower')


play()
