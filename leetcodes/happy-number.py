# ---------------------------------

# File          : happy-number.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 05/01/2026
# Modified Date : 05/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1

'''

# can be done using array and set, but set is faster than using array - array(1 ms) set(0 ms) when run on leetcodes website
def isHappy(n):
#    nlist = []
    nset = set()
    strn = str(n)
    print(strn)
#    while strn not in nlist:
#        nlist.append(strn)
#        print(nlist)
    while strn not in nset:
        nset.add(strn)
        print(nset)
        sumn = 0
        for i in strn:
            sumn = sumn + int(i)**2
            print("The sum is :",sumn)

        if sumn == 1:
            return True
        strn = str(sumn)

    return False

if __name__ == '__main__':

    n = 19

    print("The check for happy number for the integer number ",n," is :",isHappy(n))
