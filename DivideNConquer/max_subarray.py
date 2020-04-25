# Project : Finding the maximum sub-array
# Author : Shobhit Gupta
# Created : 4/11/2020
#Last Edited : 4/11/12020


# Function to find the max crossing subarray
def find_max_crossing_subarray(A,beg,mid,end):

    # Finding the max sub array left of mid
    left_sum = float('-inf')
    sum = 0
    for i in range(mid,beg-1,-1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    # Finding the max sub-array right of mid
    right_sum = float('-inf')
    sum = 0

    for i in range(mid+1,end+1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum+right_sum

# Recursive function to find the max sub-array
def find_max_subarray(A,beg,end):

    #base case - if single element, return the element
    if beg == end:
        return beg,end,A[beg]
    else:
        mid = (beg + end) // 2 #integral division

        #left part of the sub problem
        left_low, left_high, left_sum = find_max_subarray(A,beg,mid)

        #right part of the subproblem
        right_low, right_high, right_sum = find_max_subarray(A,mid+1,end)

        #crossing subarray
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A,beg,mid,end)

        #comparing the sums
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


# Running the code:
if __name__ == '__main__':
    array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

    low,high,sum = find_max_subarray(array,0,len(array)-1)

    # print("The correct answer is ({},{},{})".format(6,10,28))
    print("\nThe computed answer is ({},{},{})".format(low,high,sum))


