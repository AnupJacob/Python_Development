# ---------------------------------

# File          : Length-of-Last-Word.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 01/01/2026
# Modified Date : 01/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

'''


def lengthOfLastWord(s):
    s = s.strip()
    splitlist = s.split(" ")
    lenlist =len(splitlist)
    lastword = splitlist[lenlist-1]

    return len(lastword)


if __name__ == '__main__':
    s = "Hello World"
    print("The length of the last word is : ",lengthOfLastWord(s))
