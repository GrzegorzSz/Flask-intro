"""
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

def firstAndLast(seq, nFirst, nLast):
    return [lst[:nFirst], lst[-nLast:]]

if __name__ == '__main__':
    lst = list('mielonkajajkaszynka')
    fAl = firstAndLast(lst, 5, 2)
    print('head: %s, tail %s' % (fAl[0], fAl[1]))
