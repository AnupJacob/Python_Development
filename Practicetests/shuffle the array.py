# ---------------------------------

# File          : shuffle the array.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def shuffle(nums,k):

    p = nums[:k:1]
    q = nums[k::]
    result =[]

    for i in range(k):
        result.append(p[i])
        result.append(q[i])

    return result


if __name__ == '__main__':
    nums = [1,2,3,4,4,3,2,1]
    k = 4
    print("The shuffled array is ",shuffle(nums,k))