# ---------------------------------

# File          : longest-common-prefix.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/01/2026
# Modified Date : 02/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

'''

def longestCommonPrefix(strs):
    first = min(strs)
    last = max(strs)
    ans = ""
    i = 0

    while i < len(first) and first[i] == last[i]:
        ans = ans + first[i]
        i += 1

    return ans


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print("The longest common prefix for the given list \"",strs,"\" is ",longestCommonPrefix(strs))