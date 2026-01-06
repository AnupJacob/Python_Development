# ---------------------------------

# File          : longest-substring-without-repeating-characters.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 06/01/2026
# Modified Date : 06/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''
'''
#brute force solution
def lengthOfLongestSubstring(s):
    strlen = len(s)
    maxcount = 0
    for i in range (strlen):
        strset = set()
        for j in range(i,strlen):
            if s[j] not in strset:
                strset.add(s[j])
                maxcount = max(maxcount,j-i+1)
            else:
                break

    return maxcount
'''
#optimised solution using sliding window
def lengthOfLongestSubstring(s):
    strlen = len(s)
    strset = set()
    maxcount = 0
    left = 0

    for right in range(strlen):
        while s[right] in strset:
            strset.remove(s[left])
            left += 1
        strset.add(s[right])
        maxcount = max(maxcount,right-left+1)

    return maxcount

if __name__ == '__main__':
    s = "abcabcbb"
#    s = "aab"
    s = "pwwkew"
    print("The length of the longest substring is : ",lengthOfLongestSubstring(s))
