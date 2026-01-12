# ---------------------------------

# File          : valid_palidrome.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def isPalindrome(s):
    s = s.lower()
    slist = list()
    for i in s:
        if i.isalnum():
            slist.append(i)
    print(slist)

    revlist = slist[::-1]
    print(revlist)

    return revlist == slist


if __name__ == '__main__':
#    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print("The status check for validity of palindrome for the string \"",s,"\" is : ",isPalindrome(s))
