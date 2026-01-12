# ---------------------------------

# File          : anagram_test.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------
'''
#using sort function
def isAnagram(s,t):
    slist = list(s)
    slist.sort()
    tlist = list(t)
    tlist.sort()

    return slist == tlist
'''
#using sorted function
def isAnagram(s,t):
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print("Anagram check for the two strings provided is :",isAnagram(s,t))
