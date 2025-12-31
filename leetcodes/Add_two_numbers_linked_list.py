# ---------------------------------

# File          : Add_two_numbers_linked_list.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 31/12/2025
# Modified Date : 31/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

def addTwoNumbers(l1, l2):
    l1rev = []
    l2rev = []
    resultlist = []
    suml1 = suml2 = 0
    print("The two lists are: ")
    print("L1: ",l1)
    for i in reversed(l1):
        l1rev.append(i)
        suml1 = suml1*10 + i
        print(suml1)
    for j in reversed(l2):
        l2rev.append(j)
        suml2 = suml2*10 + j
        print(suml2)
    sumlist = suml1 + suml2
    print("Sum of the list is :",sumlist)

    for i in range(len(str(sumlist))):
        remnum = sumlist%10
        sumlist = sumlist // 10
        resultlist.append(remnum)
#    print("Reversed l1 is :",l1rev)
#    print("Reversed l2 is :",l2rev)
#    print("L2: ",l2)
    return resultlist

if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    print("The result list is :",addTwoNumbers(l1,l2))