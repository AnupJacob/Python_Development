# ---------------------------------

# File          : product-of-array-except-self
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 06/01/2026
# Modified Date : 06/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

'''

# Optimised solution
def productExceptSelf(nums):
    numlen = len(nums)
    answer = [1]*numlen
    left_prod = 1
    right_prod = 1
    for i in range(numlen):
        answer[i] = left_prod
        left_prod *= nums[i]
    for j in range(numlen-1, -1,-1):
        answer[j] *= right_prod
        right_prod *= nums[j]

    return answer

if __name__ == '__main__':

    nums = [-1,1,0,-3,3]
    print("The product array result is :",productExceptSelf(nums))
