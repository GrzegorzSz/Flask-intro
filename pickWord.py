"""
This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words from
the SOWPODS dictionary. Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
"""
import random

def findWord(openFile, number):
    for count in range(number):
        openFile.readline()
    return openFile.readline()

def wordsCount(openFile):
    counter = 0
    for line in openFile:
        counter += 1
    return counter

def pickWord():
    wordsFile = open('sowpods.txt')
    rand = random.randint(0, wordsCount(wordsFile))
    wordsFile.seek(0)
    drawnWord = findWord(wordsFile, rand)
    wordsFile.close()
    return drawnWord.strip()

if __name__ == '__main__':
    print(pickWord())