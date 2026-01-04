# ---------------------------------

# File          : valid-palindrome
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 04/01/2026
# Modified Date : 04/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''

''' Brute force solution
def isPalindrome(s):
    concat_strs = ''
    for i in s.lower():
        if i.isalnum():
            concat_strs = concat_strs +i
    rev_strs = reversed(concat_strs)
    print(concat_strs)

    lens = len(concat_strs)-1

    rev_strs = ''
#    for j in reversed(concat_strs):
    for j in range (lens, -1,-1):
        rev_strs = rev_strs + concat_strs[j]

    print(rev_strs)

    if rev_strs == concat_strs:
        return True
    else:
        return False

'''
def isPalindrome(s):
    concat_strs = []
    rev_strs = []
    for i in s.lower():
        if i.isalnum():
            concat_strs.append(i)
    for j in reversed(concat_strs):
        rev_strs.append(j)

    if rev_strs == concat_strs:
        return True
    else:
        return False

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
#    s = "race a car"
    print("The check for the sentence ",s," is :",isPalindrome(s))
