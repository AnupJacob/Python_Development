# ---------------------------------

# File          : merge-two-sorted-lists.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 08/01/2026
# Modified Date : 08/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------
'''

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1,list2):
        dummyNode = ListNode(-1)
        temp = dummyNode
        current1 = list1
        current2 = list2
        while current1 and current2:
            if current1.val < current2.val:
                temp.next = current1
                current1 = current1.next
            else:
                temp.next = current2
                current2 = current2.next
            temp = temp.next

        temp.next = current1 if current1 else current2

        return  dummyNode.next

def printlist(head):
    current = head
    while current:
        print(current.val,end=" -> " if current.next else " ")
        current = current.next
    print(" -> Null")

if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(4)

    node21 = ListNode(1)
    node22 = ListNode(3)
    node23 = ListNode(4)

    node11.next = node12
    node12.next = node13

    node21.next = node22
    node22.next = node23

    printlist(node11)
    printlist(node21)

    printlist(Solution.mergeTwoLists(node11,node22))