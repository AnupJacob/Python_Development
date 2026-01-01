# ---------------------------------

# File          : square-root-with-no-functions.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 01/01/2026
# Modified Date : 01/01/2026
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

def mySqrt(x):
    result = round(x ** 0.5)

    return result

if __name__ == '__main__':

    x = int(input("Enter the number for square root is to be calculated :"))
    print("The square root of the number ",x," is : ",mySqrt(x))