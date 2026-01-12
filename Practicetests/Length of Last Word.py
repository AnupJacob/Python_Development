# ---------------------------------

# File          : Length of Last Word.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/01/2026
# Modified Date : 12/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

# Optimal solution for the program
def lengthOfLastWord(s):
    words = (s.strip()).split(" ")
    wordlen = len(words)
    return len(words[wordlen-1])


if __name__ == '__main__':
    s = "Hello World"
    print("The length of the last word is : ",lengthOfLastWord(s))
