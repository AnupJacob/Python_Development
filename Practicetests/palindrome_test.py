# ---------------------------------

# File          : palindorme_test.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def isPalindrome(x):
    if x < 0:
        return False
    strx = str(x)
    revx = strx[::-1]

    return revx == strx


if __name__ == '__main__':
    x = 123421
    print("The status check for palindrome for the number ",x," is : ",isPalindrome(x))
