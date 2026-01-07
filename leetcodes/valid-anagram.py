# ---------------------------------

# File          : valid-anagram.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 07/01/2026
# Modified Date : 07/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''

# Brute force solution
def isAnagram(s,t):

    slenlist = len(s)
    tlenlist = len(t)
    slist = list(s)
    tlist = list(t)
    if slenlist == tlenlist:
        print(slist)
        print(tlist)
        tsort = sorted(tlist)
        ssort = sorted(slist)
        print(tsort)
        print(ssort)
        if tsort == ssort:
            return True
    else:
        return False

    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    print(" The given strings ",s," and ",t," is a ",isAnagram(s,t)," anagram")
