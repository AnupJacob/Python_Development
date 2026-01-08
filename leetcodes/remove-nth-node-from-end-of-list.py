# ---------------------------------

# File          : remove-nth-node-from-end-of-list.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 08/01/2026
# Modified Date : 08/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
-----------
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(head,n):
        return

def printlist(self):
    current =self
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print(" -> Null")

if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    n = 2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    printlist(node1)
#    removeNthFromEnd(head,n)
