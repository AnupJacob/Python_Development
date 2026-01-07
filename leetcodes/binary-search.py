# ---------------------------------

# File          : binary-search.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 07/01/2026
# Modified Date : 07/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''
'''
#brute force solution using for loop
def search(nums,target):
    if target not in nums:
        return -1
    for j in range(len(nums)):
        if target == nums[j]:
            return j
'''

#Brute force soultion using while loop
def search(nums,target):
    i = 0
    while i <= len(nums):
        if target == nums[i]:
            return i
        i +=1
    return target

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    print("The number ",target," can be found in the position - ",search(nums,target))
