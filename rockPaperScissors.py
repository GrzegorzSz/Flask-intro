"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
 print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""


def askTheMove():
    print('\n1 - paper\n2 - rock\n3 - scissors')
    return int(input('Your choice: '))


def validate(list):
    result = True
    goodChoices = [1, 2, 3]
    for item in list:
        if item not in goodChoices:
            result = False
    return result


def play():
    player1 = askTheMove()
    player2 = askTheMove()
    if validate([player1, player2]):
        if player1 == player2:
            print('remis')
        elif player1 == 1 and player2 == 2:
            print('player1 wins!')
        elif player1 == 2 and player2 == 3:
            print('player1 wins!')
        elif player1 == 3 and player2 == 1:
            print('player1 wins!')
        else:
            print('player2 wins!')
    else:
        print('Wrong choice\n')
        play()


while True:
    play()
    again = input('Ones again? (y/n): ')
    if again != 'y':
        break
