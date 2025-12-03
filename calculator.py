def addresult(input1, input2):
    return input1 + input2
def diffresult(input1, input2):
    return input1 - input2
def mulresult(input1, input2):
    return input1 * input2
def modresult(input1, input2):
    return input1 % input2
def divresult(input1, input2):
    return input1 / input2

def calculation():
    oper=input("Please enter the operation you want to perform: ")
    if(oper not in ('*', '-','%','+','/')):
        print('The input you provided is not supported by the application. Please try again')
        calculation()

    input1 = int(input("Please enter the first number: "))
    input2 = int(input("Please enter the second number: "))

    if (oper == '+'):
        print('The sum of the ',input1,' and ',input2,' is :',addresult(input1, input2))
    elif (oper == '-'):
        print('The difference of the ',input1,' and ',input2,' is :',diffresult(input1, input2))
    elif (oper == '*'):
        print('The multiplication of the ',input1,' and ',input2,' is :',mulresult(input1, input2))
    elif (oper == '/'):
        print('The division of the ',input1,' and ',input2,' is :',divresult(input1, input2))
    elif (oper == '%'):
        print('The reminder of the ',input1,' and ',input2,' is :',modresult(input1, input2))

    status = input("Do you want to continue? (Y/N):")
    if (status == 'Y') or (status == 'y'):
        calculation()
    elif (status != 'N') or (status == 'n'):
        print("Wrong input, please try again later")


if __name__ == '__main__':
    calculation()

    print("Thank you for using my calculator application")







