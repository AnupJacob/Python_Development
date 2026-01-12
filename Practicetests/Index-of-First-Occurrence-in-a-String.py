# ---------------------------------

# File          : 
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  :  
# Modified Date : 
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def strStr(haystack, needle):

    if needle not in haystack:
        return -1

    return haystack.find(needle)


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print("The first occurence is at position :",strStr(haystack,needle))
