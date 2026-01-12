# ---------------------------------

# File          : Search-in-Rotated-Sorted-Array.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def search(nums, target):
    dictnums = {}

    for i in range(len(nums)):
        dictnums[i] = nums[i]
        if nums[i] == target:
            return i

    return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    #    nums = [1]
    target = 1
    print("The searched element is in position :", search(nums, target))
