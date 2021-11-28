"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list
of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any other number.)
"""


def readNumFromFile(opFile):
    numbs = []
    for line in opFile:
        numbs.append(line[:-1])
    return numbs


def findOverlapingItems(openfile1, openfile2):
    numbersFile1 = readNumFromFile(openfile1)
    numbersFile2 = readNumFromFile(openfile2)
    return [int(item) for item in numbersFile1 if item in numbersFile2]


primenumbers = open('primenumbers.txt')
happynumbers = open('happynumbers.txt')
print('Primes and happy:', findOverlapingItems(primenumbers, happynumbers))
primenumbers.close()
happynumbers.close()
