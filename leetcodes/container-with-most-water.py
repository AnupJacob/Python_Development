# ---------------------------------

# File          : container-with-most-water.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 06/01/2026
# Modified Date : 06/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''
# Optimised solution
def maxArea(height):
    i = 0
    j = len(height) - 1
    maxarea = 0
    print("i = ",i)
    print("j = ",j)
    print(height)
    while i <= j:
        if height[i] > height[j]:
            area = (j-1) * height[j]
            j -= 1
        else:
            area = (j-i) * height[i]
            i += 1
        if area > maxarea:
            maxarea = area

    print(maxarea)

    return maxarea



if __name__ == '__main__':

    height = [1,8,6,2,5,4,8,3,7]

    print("The Maximum area which can withhold the water is : ",maxArea(height))
