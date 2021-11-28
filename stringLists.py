"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

userStr = input('type a word: ')
if userStr == userStr[::-1]:
    print('This word is a palindrome')
else:
    print("This word isn't a palindrome")