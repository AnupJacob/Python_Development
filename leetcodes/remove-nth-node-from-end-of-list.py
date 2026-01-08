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

#Brute force solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
#This removes the nth element from the begining and not the end, so rework required
    def removeNthFromEnd(head,n):
        current = head
        count = 0
        while current and current.next:
            count += 1
            if count == n:
                current.next = current.next.next
            current = current.next
'''
#Optimal solution
    def removeNthFromEnd(head, n):
        first = head
        last = head

        for i in range(n):
            first = first.next

        if not first:
            return head.next

        while first.next:
            last = last.next
            first = first.next

        last.next = last.next.next
        return head

def printlist(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print(" -> Null")

if __name__ == '__main__':
#    n = 2
    n = 1
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
    Solution.removeNthFromEnd(node1, n)
    printlist(node1)
