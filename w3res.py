import glob
import os.path
import time
from copy import copy
from functools import reduce

print('-' * 80)
# 106. Write a Python program to divide a path on the extension separator.
for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    print('"%s" :' % path, os.path.splitext(path))
print('-' * 80)
# 107. Write a Python program to retrieve file properties.
print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
print('-' * 80)
# 108. Write a Python program to find path refers to a file or directory when you encounter a path name.
for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
print('-' * 80)
user_num = -1.10
if user_num < 0:
    print('Negative value')
elif user_num == 0:
    print('Value is zero')
else:
    print('Positive value')
print('-' * 80)
# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
lista = [3, 15, 14, 23, 30, 45, 1]
result = list(filter(lambda x: (x % 15 == 0), lista))
print('numbers divisible by 15:', result)
print('-' * 80)
# 111. Write a Python program to make file lists from current directory using a wildcard.
file_list = glob.glob('*.*')
print(file_list)
print('-' * 80)
# 112. Write a Python program to remove the first item from a specified list.
if len(file_list) > 0:
    file_list.pop(0)            # using list method
    del file_list[0]            # using del keyword
print(file_list)
print('-' * 80)
# 113. Write a Python program to input a number, if it is not a number generate an error message.
# try:
#     float(input('Give a number: '))
# except ValueError:
#     print('This is not a number')
print('-' * 80)
# 114. Write a Python program to filter the positive numbers from a list
nums = [34, 1, 0, -23]
print('Full list', nums)
print('Positive nums:', list(filter(lambda item: (item > 0), nums)))
print('-' * 80)
# 115. Write a Python program to compute the product of a list of integers (without using for loop).
nums = [10, 20, 30,]
nums_product = reduce( (lambda x, y: x * y), nums)
print("Product of the numbers : ",nums_product)
print('-' * 80)
#  Write a Python program to print Unicode characters.
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077' \
      u'\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print(str)
print('-' * 80)
# 117. Write a Python program to prove that two string variables of same value point same memory location.
str = 'w3resource'
stra = 'w3resource'
print('str  address:', hex(id(str)))
print('stra address:', hex(id(stra)))
print('-' * 80)
# 118. Write a Python program to create a bytearray from a list.
nums = [10, 20, 56, 35, 17, 99]
btarray = bytearray(nums)
for bt in btarray: print(bt)
print('-' * 80)
# 119. Write a Python program to display a floating number in specified numbers.
order_amt = 212.374
print('The total order amount comes to %f' % order_amt)
print('The total order amount comes to %.1f' % order_amt)
print('-' * 80)
# 120. Write a Python program to format a specified string to limit the number of characters to 6.
print('%.6s' % str)
print('-' * 80)
# 121. Write a Python program to determine whether variable is defined or not
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
print('-' * 80)
# 122. Write a Python program to empty a variable without destroying it.
n = 20
d = {"x" : 200}
print(d, n)
n = type(n)()
d = type(d)()
print(d, n)
print('-' * 80)
