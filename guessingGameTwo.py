"""
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number
between 0 and 100. The program will guess a number, and you, the user, will say whether it is too
high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.
As the writer of this program, you will have to choose how your program will strategically guess.
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until
you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be
to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed.
After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is
the optimal one next week with the solution.)
"""


def askHint(number):
    print('My number is:', number)
    print('Are your number less than my [1], greater than my [2], or the numbers are equal [3]?')
    return int(input('Your answer: '))


def guessGame():
    answerSet = list(range(1, 101))
    beginMarker = 0
    endMarker = len(answerSet) - 1
    attemptsCounter = 0

    while True:
        guessMarker = (beginMarker + endMarker) // 2
        attemptsCounter += 1
        print('Attempts:', attemptsCounter)
        userAnswer = askHint(answerSet[guessMarker])
        if userAnswer == 1:
            endMarker = guessMarker - 1
        elif userAnswer == 2:
            beginMarker = guessMarker + 1
        elif userAnswer == 3:
            print('Attempts:', attemptsCounter)
            break
        else:
            print('wrong answer!')
            askHint(answerSet[guessMarker])
        if beginMarker > endMarker:
            print('Liar!')
            break


if __name__ == '__main__':
    guessGame()
