# ---------------------------------

# File          : top-k-frequent-elements.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 09/01/2026
# Modified Date : 09/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]



Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].

'''

def topKFrequent(nums,k):

    return True



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    print("The top frequent ",k," number of elements in the given list are : ",topKFrequent(nums,k))
