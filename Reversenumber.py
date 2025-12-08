# ---------------------------------

# File          : Reversenumber.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 08/12/2025
# Modified Date : 08/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def modoper(num):
    modnum = num%10
    return modnum

def reversenum(numinput):
    result = 0

    lennum = len(str(numinput))
    print("Length of the number ",numinput," is ",lennum)
    for i in range(0,lennum):
        result = result*10 + modoper(numinput)
        numinput = numinput // 10

    return result

if __name__ == '__main__':

    numinput = int(input("Enter the number to be reversed :"))

    print("Reverse of the number ",numinput," is :",reversenum(numinput))