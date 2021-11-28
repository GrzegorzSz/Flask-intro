"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have
a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list
"""
import random

words = open('/home/zolw/Downloads/pl_PL.dic', encoding='utf8')
count = 0

for line in words:
    count += 1


def generate(dicOpenFile, wordscounter, strength='weak'):
    passwd = ''
    numbers = [item for item in range(1, 100)]
    rndnumber = None
    if strength == 'weak':
        dicOpenFile.seek(random.randint(0, wordscounter))
        passwd += dicOpenFile.readline().strip()
        dicOpenFile.seek(random.randint(0, wordscounter))
        passwd += dicOpenFile.readline().strip()
        passwd = passwd.replace(' ', '')
        passwd = passwd.replace('\n', '')
        passwd = passwd.replace('/', '')
        passwd = passwd.lower()
    if strength == 'strong':
        passwd = ''
        passlist = None
        while len(passwd) < 8:
            dicOpenFile.seek(random.randint(0, wordscounter))
            passwd += dicOpenFile.readline().strip()
        passwd = passwd.replace(' ', '')
        passwd = passwd.replace('\n', '')
        passwd = passwd.replace('/', '')
        rndnumber = random.randint(1, len(passwd))
        passwd = passwd[:rndnumber] + str(random.randint(0, len(numbers))) + passwd[rndnumber:]
        passwd = passwd.lower()
        passlist = list(passwd)
        for quantity in range(random.randint(1, int(len(passlist)/2))):
            position = random.randint(0, len(passlist))
            passlist[position] = passlist[position].upper()
        passwd = ''
        for item in passlist:
            passwd += item
    return passwd


print(generate(words, count))
print(generate(words, count, 'strong'))
words.close()
