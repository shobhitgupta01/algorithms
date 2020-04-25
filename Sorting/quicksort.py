# Project : Program to perform quicksort
# Author : Shobhit Gupta


# Partition Subroutine
def partition(A,p,r):
    """
    :param A: Array
    :param p: starting index
    :param r: ending index
    :return: index of fixed pivot
    """
    # pivot element
    x = A[r]

    i = p-1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            # swapping A[i] and A[j]
            A[i],A[j] = A[j],A[i]

    # fixing position of the pivot element
    A[i+1],A[r] = A[r],A[i+1]

    return i+1

# method to perform quicksort

def quicksort(A, p, r):
    """
    Method to perform quicksort
    :param A: Input array
    :param p: starting index
    :param r: ending index
    :return: sorted array
    """
    if p < r :
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

if __name__ == '__main__':
    A = [1,9,2,8,3,8,4,7,5,6]
    quicksort(A,0,len(A)-1)
    print("Sorted Array is {}".format(A))
