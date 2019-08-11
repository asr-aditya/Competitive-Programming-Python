


    # @param A : tuple of list of integers
    # @return a list of integers
def spiralOrder(A):
    T = 0
    B = len(A)
    L = 0
    R = len(A[0])
    dirr = 0

    while(T<=B and L <= R):

        if dirr == 0:
            i = L
            while i < R :
                print(A[T][i])
                i = i + 1
            T = T + 1
            #print("T = ", T)
            #dirr = 1

        if dirr == 1:
            i = T
            while i < B:
                print(A[i][R-1])
                i = i + 1
            R = R - 1
            #print("R = ", R)
            #dirr = 2

        if dirr == 2:
            i = R - 1
            while i >= L :
                print(A[B-1][i])
                i = i - 1
            B = B - 1
            #print("B = ", B)
            #dirr = 3

        if dirr == 3:
            i = B - 1
            while i >= T :
                print(A[i][L])
                i = i - 1
            L = L + 1
            #print("L = ", L)
            #dirr = 0
        dirr = (dirr + 1) % 4
        #print("dirr = ", dirr)


spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
