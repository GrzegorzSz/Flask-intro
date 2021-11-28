"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    1. Randomly generate two lists to test this
    2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
from random import randint

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def findCommons(seq1, seq2):
    common = [item for item in seq1 if item in seq2]
    return list(set(common))


def makeRandomList():
    rndlist = []
    for x in range(randint(8, 40)):
        rndlist.append(randint(0, 100))
    return rndlist


print('Common elements:', findCommons(list1, list2))
print('randomize...')
rndList1 = makeRandomList()
rndList2 = makeRandomList()
print(sorted(rndList1))
print(sorted(rndList2))
print('Common elements of random lists:', findCommons(rndList1, rndList2))


test = list(set(list1).intersection(set(list2)))
if test:
    print("The intersections are: ", test)
else:
    print("No intersection.")