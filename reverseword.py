# ---------------------------------

# File          : reverseword.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 29/12/2025
# Modified Date : 29/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------


if __name__ == '__main__':

    word = input("Enter the word to be reversed: ")
    wordlen = len(word)
    print("The length of the word is ",wordlen)
    print("The word to be reversed is", word)
    reverseword = []
    for i in range(wordlen,0,-1):
        print(word[i-1])
        reverseword.append(word[i-1])

    reverseword = ''.join(reverseword)
    revword2 = ''.join(reversed(word))
    print("The reverse of the word is ", reverseword)
    print("The reverse operation by function gives: ", revword2)