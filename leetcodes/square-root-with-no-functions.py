# ---------------------------------

# File          : square-root-with-no-functions.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 01/01/2026
# Modified Date : 01/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

#optimised solution:

def mySqrt(x):
    if x == 0 or x == 1:
        return x

    start = 1
    end = x
    while start <= end:
        mid = (start + end)//2
        if mid * mid == x:
            return mid
        elif mid*mid < x:
            start = mid + 1
        elif mid*mid > x:
            end = mid - 1
    return end

if __name__ == '__main__':

    x = int(input("Enter the number for square root is to be calculated : "))
    print("The square root of the number ",x," is : ",mySqrt(x))