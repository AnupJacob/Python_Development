# ---------------------------------

# File          : arrarsum.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 29/12/2025
# Modified Date : 29/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def arraysum(array1):
    result = 0

    for i in array1:
        result = result + i

    return result


if __name__ == '__main__':
    array1 = list(map(int,input("Enter the array elements: ").split(' ')))
    print("The array you entered is ",array1)

    arraylen = len(array1)

    print("The sum of the ",arraylen," array elements is: ",arraysum(array1))

