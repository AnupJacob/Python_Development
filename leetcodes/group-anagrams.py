# ---------------------------------

# File          : group-anagrams.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 09/01/2026
# Modified Date : 09/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''

def groupAnagrams(strs):

    return strs


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("The grouped anagrams are :",groupAnagrams(strs))
