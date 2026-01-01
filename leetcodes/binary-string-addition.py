# ---------------------------------

# File          : binary-string-addition.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 01/01/2026
# Modified Date : 01/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------
'''

Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

def addBinary(a,b):
    lena =len(a)
    lenb = len(b)
    print(lena)
    print(lenb)
    carry = 0
    resultlist =[]
    for i in range(lena):
        for j in range(lenb):
            if i == j:
                print("I value of :",i)
                print("a[",i,"] : ",a[i])
                print("b[",j,"] : ",b[j])
                print("carry : ",carry)
                print("**************************")
                if carry == 0:
                    if a[i] == 1 and b[j] == 1:
                            resultlist.append(0)
                            carry += 1
                    elif a[i] == 1 and b[j] == 0:
                            resultlist.append(1)
                    elif a[i] == 0 and b[j] == 1:
                            resultlist.append(1)
                    elif a[i] == 0 and b[j] == 0:
                            resultlist.append(0)
                elif carry == 1:
                    if a[i] == 1 and b[j] == 1:
                            resultlist.append(1)
                            carry += 1
                    elif a[i] == 1 and b[j] == 0:
                            resultlist.append(0)
                            carry += 1
                    elif a[i] == 0 and b[j] == 1:
                            resultlist.append(0)
                            carry += 1
                    elif a[i] == 0 and b[j] == 0:
                            resultlist.append(1)
    print(resultlist)

    return


if __name__ == '__main__':
    a = '1010'
    b = '1011'
    print("The binary string after addition is : ",addBinary(a,b))
