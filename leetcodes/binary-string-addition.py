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
    print("Binary strings are :",a," and ",b)
    reva = ''.join(reversed(a))
    revb = ''.join(reversed(b))
    print(reva)
    print(revb)
    carry = 0
    resultlist =[]
    for i in range(lena):
        for j in range(lenb):
            if i == j:
                print("a[",i,"] : ",reva[i])
                print("b[",j,"] : ",revb[j])
                print("carry : ",carry)
                print("**************************")
                if carry == 0:
                    print("Carry 0")
                    if reva[i] == '1' and revb[j] == '1':
                        resultlist.append(0)
                        carry = 1
                    elif reva[i] == '1' and revb[j] == '0':
                        resultlist.append(1)
                    elif reva[i] == '0' and revb[j] == '1':
                        resultlist.append(1)
                    elif reva[i] == '0' and revb[j] == '0':
                        resultlist.append(0)
                elif carry == 1:
                    print("Carry 1")
                    if reva[i] == '1' and revb[j] == '1':
                        resultlist.append(1)
                        carry = 1
                    elif reva[i] == '1' and revb[j] == '0':
                        resultlist.append(0)
                        carry = 1
                    elif reva[i] == '0' and revb[j] == '1':
                        resultlist.append(0)
                        carry = 1
                    elif reva[i] == '0' and revb[j] == '0':
                        resultlist.append(1)
    print(resultlist)

    return resultlist


if __name__ == '__main__':
    a = '11'
    b = '1'
    print("The binary string after addition is : ",addBinary(a,b))
