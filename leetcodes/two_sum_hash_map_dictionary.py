# ---------------------------------

# File          : two_sum_hash_map_dictionary.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 30/12/2025
# Modified Date : 30/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOPs
# ----------------------------------

'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''

def hashmaptwosum(numlist, target):

#    dict1 = {}
    print(numlist)
    print(len(numlist))

    result = {}

    for i, num in enumerate(numlist):
        diff = target - num
        if diff in result:
            print(result[diff], i)
            break
        result[num] = i


'''
    for i in range(len(numlist)):
        temp = i
        if (target - numlist[i]) in numlist :
            dict1[i] = numlist[i]
            result.append(i)
            print("Number: ",numlist[i]," at position : ",i)
'''





if __name__ == '__main__':
    nums = [2,7,11,15]
#    nums = [3,3]
#    nums = [3,2,4]
#    target = 6
    target = 9

    hashmaptwosum(nums,target)

    print("The sum leading to the target : ",target," exists.")