# Project : Heap Sort Algorithm
# Author : Shobhit Gupta


def left(i):
    """
    :param i: index of a node in heap
    :return: index of the root of the left subtree of i
    """
    return 2 * (i+1) - 1


def right(i):
    """
    :param i: index of a node in heap
    :return: index of the root of the right subtree of i
    """
    return (2 * (i+1))


def max_heapify(A, i):
    """
    :param A: Dictionary with array which can be represented as heap
    :param i: index of element to be inserted to restore max_heap
    :return: nothing
    """
    l = left(i)
    r = right(i)

    # checking if left subtree root value is greater
    if l <= A['heap_size'] - 1 and A['values'][l] > A['values'][i]:
        largest = l
    else:
        largest = i
    # checking if right subtree root value is greater
    if r <= A['heap_size'] - 1 and A['values'][r] > A['values'][largest]:
        largest = r

    # swapping if A[i] is not the largest
    if largest != i:
        # swapping the values
        A['values'][i] = A['values'][i] + A['values'][largest]
        A['values'][largest] = A['values'][i] - A['values'][largest]
        A['values'][i] = A['values'][i] - A['values'][largest]

        # recursive call to the subtree
        max_heapify(A, largest)

def build_max_heap(A):
    """
    :param A: Array to be converted into max_heap
    :return: Max heap
    """
    for i in range(len(A['values']) // 2,0,-1):
        max_heapify(A, i-1)

def heap_sort(A):
    # building the max heap out of the array A
    build_max_heap(A)

    for n in range(len(A['values']),1,-1):

        #swap the first element with last as first element is max
        temp = A['values'][0]
        A['values'][0] = A['values'][n-1]
        A['values'][n-1] = temp

        # reduce the heap size
        A['heap_size'] -= 1

        # max_heapify the tree so that the max element comes on top
        max_heapify(A,0)


if __name__ == '__main__':
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    B = {'heap_size': len(A),'values': A}
    heap_sort(B)
    print("The sorted array is {}".format(B['values']))
    print("\nThe heap dict is {}".format(B))
