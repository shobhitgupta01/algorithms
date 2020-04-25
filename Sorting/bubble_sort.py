def bubble_sort(A):
    '''

    :param A: unsorted array
    '''

    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i] > A[j]:
                #swap
                temp = A[i]
                A[i] = A[j]
                A[j] = temp


if __name__ == '__main__':
    arr = list(map(int,input("Enter an unsorted array\n").split()))
    print("The input array is ",arr)
    bubble_sort(arr)
    print("The sorted array is ",arr)