def addTwoNumbers(l1, l2):
    sum2 = 0
    sum1 = 0
    print("l1 is :", l1)
    print("l2 is :", l2)
    for i in range(len(l1)):
        sum1 = sum1+l1[i]*10**i
    for j in range(len(l2)):
        sum2 = sum2+l2[j]*10**j
    print(sum1+sum2)
    return sum

if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    print("Sum of the linked list is ", addTwoNumbers(l1,l2))