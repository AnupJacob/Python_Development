# ---------------------------------

# File          : happy_number_test.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------
#Program written to test if the logic has same time/ space complexity as used by list, where leetcode pgm written using set in my previous solution
def isHappy(n):
    nlist = list()
    strn = str(n)

    while strn not in nlist:
        sumn = 0
        for i in strn:
            sumn = sumn + pow(int(i),2)
            print(i)
            print(sumn)

        if sumn == 1:
            return True
        strn = str(sumn)

    return False


if __name__ == '__main__':
    n = 19
    print("The status of happy number check for the number ",n," is : ",isHappy(n))
