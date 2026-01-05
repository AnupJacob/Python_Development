# ---------------------------------

# File          : remove-duplicates-from-sorted-linked-list.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 05/01/2026
# Modified Date : 05/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

'''

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(head):
        if not head:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    if __name__ == '__main__':
        node1 = ListNode(1)
        node2 = ListNode(1)
        node3 = ListNode(2)
        node4 = ListNode(3)
        node5 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5


