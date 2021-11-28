"""
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes care of for us.
All you need is some variables and if statements!
"""


def takeVal():
    value = ''
    isFloat = False
    while not isFloat:
        value = input('Give a number: ')
        try:
            value = float(value)
            isFloat = True
        except ValueError:
            isFloat = False
    return float(value)


def findLargest(val):
    max = val[0]
    for item in val:
        if item > max:
            max = item
    return max


def start():
    userVals = []
    for counter in range(3):
        userVals.append(takeVal())
    print('taken values: ', userVals)
    print('largest is:', findLargest(userVals))


start()
