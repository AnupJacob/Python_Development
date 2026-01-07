# ---------------------------------

# File          : kth-largest-element-in-an-array
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 07/01/2026
# Modified Date : 07/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

'''
def findKthLargest(nums,k):

    return k


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print("The k = ",k," largest number in the array is :",findKthLargest(nums,k))
