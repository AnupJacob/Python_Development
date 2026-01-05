# ---------------------------------

# File          : Single-Number.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 05/01/2026
# Modified Date : 05/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1



Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

'''

#Brute force solution
def singleNumber(nums):
    list = []
    for i in nums:
        if i not in list:
            list.append(i)
            print(i," - First time found in the list, so adding to the arraylist")
        else:
            print(i," is already in the list. Therefore not eligible")
            list.remove(i)
    strnum = ""
    for j in list:
        strnum = strnum + str(j)
    return strnum


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print("The single number with no duplicates is : ",singleNumber(nums))
