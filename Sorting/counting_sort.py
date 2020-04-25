# Project : Counting Sort
# Author : Shobhit Gupta


def counting_sort(A):
    """
    This method implements counting sort algorithm
    :param A: input unsorted array
    :return: sorted array
    """
    # getting the max value from the array A
    maximum = max(A)

    # creating an indexing array
    C = [0 for i in range(maximum+1)]  # created array of length max+1

    # creating the output array
    B = [0 for i in range(len(A))]

    # storing the frequency of every element in A
    for element in A:
        C[element] += 1

    # adding the prev freq value in C to find relative position in V
    for i in range(1,len(C)):
        C[i] = C[i] + C[i-1]

    # placing the array elements into the correct position
    for i in range(len(A)):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1

    return B


if __name__ == '__main__':
    unsorted_array = [1,9,2,8,3,7,3,6,5]
    sorted_array = counting_sort(unsorted_array)
    print("The sorted array is {}".format(sorted_array))


