# ---------------------------------

# File          : arraytest.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 07/12/2025
# Modified Date : 07/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------


if __name__ == '__main__':

    numarray = input("Enter elements separated by space: ").split()
    lenarray = len(numarray)

    print("The length of the array is :",lenarray)

    sumarray = 0
    mularray = 1

    for i in range(0,lenarray):
        sumarray = sumarray + int(numarray[i])
        mularray = mularray * int(numarray[i])

    print("The sum of the array elements is :",sumarray)
    print("The product of the array elements is :",mularray)