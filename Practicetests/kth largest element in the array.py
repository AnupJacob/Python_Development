# ---------------------------------

# File          : kth largest element in the array
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def findKthLargest(nums, k):
    sortednum = sorted(nums, reverse=True)
    return sortednum[k-1]

if __name__ == '__main__':
#    nums = [3, 2, 1, 5, 6, 4]
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
#    k = 2
    print("The kth largest element in the array - ",nums," is : ",findKthLargest(nums, k))
