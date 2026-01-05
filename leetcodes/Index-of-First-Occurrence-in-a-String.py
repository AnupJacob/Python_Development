# ---------------------------------

# File          : Index-of-First-Occurrence-in-a-String.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 05/01/2026
# Modified Date : 05/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

'''

def strStr(haystack, needle):

    return 1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print("The first occurence is at position :",strStr(haystack,needle))
