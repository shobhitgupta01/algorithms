# Project   : This is the implementation of Strassen's method of square matrix multiplication
# Author    : Shobhit Gupta

#Note : We will be using numpy as it becomes easy for us to do matrix operations

import numpy as np

def split_matrix(X):
    '''

    :param X: Input numpy 2d array
    :return: Four numpy arrays
    '''
    nrows, ncols = X.shape
    rows, cols = nrows //2 , ncols // 2

    return X[:rows,:cols], X[:rows,cols:], X[rows:, :cols], X[rows:,cols:]


def recursive_square_matrix_mul(A,B):
    '''

    :param A: First square matrix (numpy array)
    :param B: Second sqaure matrix (numpy array)
    :return: Multiplied square matrix
    '''

    n = len(A)

    if n == 1:
        return A * B

    else:

        # splitting the matrices
        A11, A12, A21, A22 = split_matrix(A)
        B11, B12, B21, B22 = split_matrix(B)

        C11 = recursive_square_matrix_mul(A11, B11) + recursive_square_matrix_mul(A12, B21)
        C12 = recursive_square_matrix_mul(A11, B12) + recursive_square_matrix_mul(A12, B22)
        C21 = recursive_square_matrix_mul(A21, B11) + recursive_square_matrix_mul(A22, B21)
        C22 = recursive_square_matrix_mul(A21, B12) + recursive_square_matrix_mul(A22, B22)

        C = np.vstack((np.hstack((C11,C12)),np.hstack((C21,C22))))

        return C





if __name__ == '__main__':

    A = np.array([[1,2],[3,4]])
    B = np.array([[1,2],[3,4]])

    C = recursive_square_matrix_mul(A,B)

    print(C)


