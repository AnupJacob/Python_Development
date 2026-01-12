# ---------------------------------

# File          : twosum_test.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------
#brute force solution
def twoSum(nums,target):
    newlist = list()
    lennums = len(nums)
    for i in range(lennums):
        for j in range(lennums):
            if i != j:
                sumn = nums[i] + nums[j]
                print(sumn)
                if sumn == target:
                    newlist.append(i)
                    newlist.append(j)
                    return newlist

    return -1

if __name__ == '__main__':
    #nums = [2, 7, 11, 15]
    #target = 9
    nums = [3, 2, 4]
    target = 6

    print("The position of the two numbers adding to the number ", target," is : ",twoSum(nums,target))
