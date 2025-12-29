# ---------------------------------

# File          : calcdraft.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 29/12/2025
# Modified Date : 29/12/2025
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------


def calculate(num1, num2, oper):
    if (oper == '+'):
        result = num1 + num2
    elif (oper == '-'):
        result = num1 - num2
    elif (oper == '*'):
        result = num1 * num2
    elif (oper == '/'):
        result = num1 / num2
    elif (oper == '%'):
        result = num1 % num2
    elif (oper == '//'):
        result = num1 // num2
    else:
        result = 'Error'

    return result

if __name__ == '__main__':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    oper = input("Enter the operation (+,-,*,/,//,%): ")

    if (calculate(num1,num2,oper) == 'Error'):
        print("The operation you selected is wrong")
    else:
        print("The result of ", calculate(num1, num2, oper))

