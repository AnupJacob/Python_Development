# ---------------------------------

# File          : recursivepgm.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 29/12/2025
# Modified Date : 29/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def recursivefactorial(num):

    print(num)
    if num > 1:
        result = num * recursivefactorial(num-1)
    elif (num == 1):
        result = 1

    return result

if __name__ == '__main__':
    num = int(input("Enter the number to calculate the factorial: "))

    print("The factorial of the number is: ",recursivefactorial(num))

