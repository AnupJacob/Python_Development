# ---------------------------------

# File          : dictionary_test.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 30/12/2025
# Modified Date : 30/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def dictionarytest(dict1):
    keyinput = input("Enter the key: ")
    value = input("Enter the value: ")

    dict1[keyinput] =value

    choice = input("Do you want to continue adding more key-values to the dictionary (y/n)?")
    if choice in ('y','Y','yes', 'Yes','YES'):
        dictionarytest(dict1)
    elif choice in ('n','N','no', 'No','NO'):
        print("Ending dictionary")
    else:
        print("Wrong choice. Closing addition of dictionary now")

    return dict1

if __name__ == '__main__':
    dict1 = dict()
    print("Dictionary entered is :", dictionarytest(dict1))