# ---------------------------------

# File          : first-unique-character-in-a-string.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 09/01/2026
# Modified Date : 09/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1



Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

'''
def firstUniqChar(s):
    return True


if __name__ == '__main__':
    s = "loveleetcode"

    print("The unique character in the string lies at position : ",firstUniqChar(s))
