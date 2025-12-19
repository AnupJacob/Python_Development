# ---------------------------------

# File          : max-consecutive-ones
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 19/12/2025
# Modified Date : 19/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

'''

def findMaxConsecutiveOnes(nums):

    maxval = 0
    result = 0
    for i in nums:
        if i == 1:
            result += 1
            maxval = max(maxval,result)
        else:
            result = 0

    return maxval

if __name__ == '__main__':
    print('The maximum consecutive ones is : ',findMaxConsecutiveOnes([1,1,0,1,1,1]))