# Project   : Bucket Sort
# Author    : Shobhit Gupta

import math


def insertion_sort(A):
    """
    This function implements insertion sort
    :param A: input array
    :return: sorted array
    """
    for i in range(1,len(A)):
        key = A[i]
        pos = i - 1

        # moving the elements forward
        while(pos >=0 and A[pos] > key):
            A[pos+1] = A[pos]
            pos -= 1

        # inserting the element at correct pos
        A[pos+1] = key


def bucket_sort(A):
    """
    This function implements bucket sort
    :param A: input array with range[0,1)
    :return: sorted array
    """

    # creating bucket array
    B = [[] for i in range(10)]

    # inserting the numbers in the bucket
    for i in range(len(A)):
        B[math.floor(A[i] * 10)].append(A[i])

    # sorting all the sub arrays in the bucket
    for i in range(len(B)):
        insertion_sort(B[i])

    output = []

    for bucket in B:
        output.extend(bucket)

    for i in range(len(A)):
        A[i] = output[i]


if __name__ == '__main__':
    arr = [0.87,0.82,0.34,0.38,0.12,0.22,0.28,0.45,0.67]
    bucket_sort(arr)
    print(arr)


