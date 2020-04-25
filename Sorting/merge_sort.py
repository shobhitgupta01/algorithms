


def merge(A,p,q,r):
    '''

    :param A: Input array
    :param p: starting index
    :param q: split index
    :param r: ending index of A
    :return: Merged array
    '''

    # defining infinite value to be used as sentinel value
    pos_inf = float('inf')

    # defining temporary arrays for storing values of A

    L = [A[i] for i in range(p,q+1)]
    M = [A[i] for i in range(q+1,r+1)]

    # adding the sentinel elements
    L.append(pos_inf)
    M.append(pos_inf)

    #merging
    i=0
    j=0
    for k in range(p,r+1):
        if L[i] < M[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = M[j]
            j += 1
    # print("A after merging is ",A)



def merge_sort(A,p,r):
    '''

    :param A: input Array
    :param p: starting index
    :param r: ending index
    :return: sorted array A
    '''
    if p < r:
        # finding the split index
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)



if __name__ == '__main__':

    A = list(map(int,input("Enter an unsorted array ....\n\n").split()))
    # A = [5,4,3,2,1]
    print("Input array is ",A)
    #
    merge_sort(A,0,len(A)-1)
    #
    print("The sorted array is ",A)



