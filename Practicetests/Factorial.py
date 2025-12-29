# ---------------------------------
# File          : Factorial.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 07/12/2025
# Modified Date : 07/12/2025
# Description   : Factorial of a Number
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def Factorial(num):

    print("Inside the function with input",num)

    result = 1

    for i in range(1, num+1):

        result = result * i
        print(i)
    return result

if __name__ == '__main__':
    FactInput = int(input("Enter the number for which the factorial is to be found: "))

    print("The number entered is",FactInput)


    print("The factorial of the ",FactInput," is : ",Factorial(FactInput))