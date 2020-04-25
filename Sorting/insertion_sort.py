
def insertion(A):
    '''
    This function sorts the input array A in ascending order using insertion sort
    '''

    # starting comparison from the second element
    print("The array received is ",A)
    for i in range(1,len(A)):
        key = A[i]
        pos = i-1

        while(pos >=0 and key < A[pos]):
            A[pos+1] = A[pos]
            pos -= 1

        A[pos+1] = key

    return A



input_array = list(map(int,input("Enter an unsorted array..\n\n").split()))

print("The sorted array is ",insertion(input_array))



