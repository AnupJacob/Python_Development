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


'''
#My initial solution, 10/23 tescases passed needs checking again
from collections import Counter

def topKFrequent(nums,k):
    dictnums = {}
    numlist = list()
    count = Counter(nums)
    tempcount = 0
    newlist = list()

    for i, j in enumerate(nums):
        if j not in numlist:
            print(j, " count of : ",count[j])
            numlist.append(j)
            dictnums[j] = count[j]


            for m,n in dictnums.items():
                print(m, " : ",n)
                if tempcount < k and m not in newlist:
                    newlist.append(m)
                    tempcount += 1


    print(newlist)

    return newlist
'''
#Optimsed solution using lambda
def topKFrequent(nums,k):
    listnum = list()
    count = 0
    dictnums = {}

    for i in nums:
        dictnums[i] = dictnums.get(i, 0) + 1

    dictnums = sorted(dictnums.items(), key=lambda num: num[1], reverse=True)

    return [num[0] for num in dictnums[:k]]

if __name__ == '__main__':
    nums = [3,0,1,0]
#    nums = [1, 1, 1, 2, 2, 3]
    nums = [1,2,1,2,1,2,3,1,3,2]

    k = 2
#    k = 1

    print("The top frequent ",k," number of elements in the given list are : ",topKFrequent(nums,k))
