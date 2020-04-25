# Project   : Radix Sort
# Author    : Shobhit Gupta


# modified counting sort to sort according to decimal space
def counting_sort(A,decimal):
    """
    Counting sort which will sort according to the decimal value
    :param A: Input array
    :param decimal: the decimal space (1 for the first, 100 for the second and so on)
    :return: Sorted array
    """

    # dummy output array
    output = [0 for i in range(len(A))]

    # counting array
    count = [0 for i in range(10)]

    # storing the count of the digit at the decimal place
    for i in range(len(A)):

        # removing the preceding digits
        index = A[i]//decimal

        # getting the last digit and incrementing the count
        count[index % 10] += 1

    # finding cumulative count by adding the prev value to find the sorted position
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # getting the output array
    for i in range(len(A)):
        index = A[i]//decimal
        output[count[(index % 10)] - 1] = A[i]
        count[index % 10] -= 1

    # copying the output in the original array
    for i in range(len(output)):
        A[i] = output[i]

def radix_sort(A):
    """
    This function implements radix sort using counting sort
    :param A: Input array
    :return: sorted array
    """
    # getting the max number to find max no of digits
    maximum = max(A)

    digits = 0

    while(maximum > 0):
        maximum = maximum // 10
        digits += 1

    decimal = 1
    print("The number of digits is ",digits)
    for i in range(digits):
        counting_sort(A, decimal)
        decimal *= 10
        print("The sorted array in iteration no {} is {}".format(i+1,A))

if __name__ == '__main__':
    array = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(array)
    print("\nThe final sorted array is {}".format(array))


