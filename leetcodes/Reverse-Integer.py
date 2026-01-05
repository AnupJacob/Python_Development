# ---------------------------------

# File          : Reverse-Integer.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 05/01/2026
# Modified Date : 05/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1

'''

'''
# Brute force solution
def reverse(x):
    listx = list(str(x))
    revx = ''

    if '-' in listx:
        revx = '-' + revx
        listx.remove('-')
    listx.reverse()

    for i in listx:
        revx = revx + i

    revx = int(revx)

    print(pow(2,31))

    if (revx >= (pow(2,31)-1)) or (revx < -pow(2,31)):
        return 0

    return revx

# brute force approach 2
def reverse(x):
    revx = ''
    x = int(x)
    if (x < 0):
        revx = '-' + revx

    absx = str(abs(x))
    revx = ''.join(reversed(absx))
    revx = int(revx)

    if (revx >= (pow(2, 31) - 1)) or (revx < -(pow(2, 31))):
            return 0

    return revx

'''
def reverse(x):

    if x < 0:
        revx = -1 * int(str(x)[1:][::-1])
    else:
        revx = int(str(x)[::-1])

    if (revx >= (pow(2, 31) - 1)) or (revx < -(pow(2, 31))):
            return 0

    return revx

if __name__ == '__main__':

    x = -321
    print("The reversed signed result of the given number ",x," is : ",reverse(x))
