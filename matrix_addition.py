# ---------------------------------

# File          : matrix_addition
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 15/12/2025
# Modified Date : 15/12/2025
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

def matrixsum(mat1, mat2,lenmat):
    for i in range (0,lenmat):
        sum=int(mat1[i]) + int(mat2[i])
        print(lenmat)
        matrixsum = []
        matrixsum.append(sum)
        print(matrixsum[i])

    return(matrixsum)

if __name__ == '__main__':

    mat1 = list(input("Enter the first matrix: ").split(sep=","))
    mat2 = list(input("Enter the second matrix: ").split(sep=","))

    len1 = len(mat1)
    len2 = len(mat2)

    print(mat1)
    print(mat2)

    print("The number of array elements in matrix 1 is :", len1)
    print("The number of array elements in matrix 2 is : ",len2)

    if len1 == len2:
        print("The sum matrix is : ")
        resultmat=[]
        resultmat = matrixsum(mat1,mat2,len1)
#        for j in range(len1):
 #           print(resultmat)

    else:
        print("Sum of matrices not possible as the number of array elements of both the matrices are not equal")



    print("Thank you for using my application")