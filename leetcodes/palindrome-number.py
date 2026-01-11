# ---------------------------------

# File          : palindrome-number.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 11/01/2026
# Modified Date : 11/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

'''

'''
#Brute force solution
def isPalindrome(x):
    revlistx = list()
    if x < 0:
        return False

    listx = list(str(abs(x)))

    print(listx)

    for i in range(len(listx)-1,-1,-1):
        revlistx.append(listx[i])

    print(revlistx)

    if revlistx == listx:
        return True
    return False
'''
'''
#Brute force solution 2 using slicing
def isPalindrome(x):

    absval = str(abs(x))
    revabsx = absval[::-1]

    print(revabsx)
    if revabsx == absval:
        return True
    return False
'''
#Brute force solution 2 using slicing optimised
def isPalindrome(x):

    val = rev = str(x)
    rev = val[::-1]

    return val == rev

'''
#Better optimised solution not converting to string
def isPalindrome(x):
    rev = 0

    if x < 0:
        return False

    absx = abs(x)
    while (absx!= 0):
        rev = rev * 10 + absx % 10
        absx = absx // 10

    return rev == x
'''
if __name__ == '__main__':
    x = 121
    print("The result check for the given number ",x," is : ",isPalindrome(x))