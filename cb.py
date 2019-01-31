T = int(input())
for i in range(T):
    def printSolution(board, N,R,C,K):
        c=0
        x=[]
        y=[]
        for i in range(N):
            for j in range(N):
                if(board[i][j]==1):
                    c+=1
                    if (i not in R) and (j not in C):
                        x.append(i)
                        y.append(j)
        print(c-K,end='')
        for i in range(c-K):
            print(x[i],end='')
            print(y[i],end='')


    def isSafe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        return True


    def solveNQUtil(board, col, N):
        if col >= N:
            return True

        for i in range(N):

            if isSafe(board, i, col):

                board[i][col] = 1
                if solveNQUtil(board, col + 1,N) == True:
                    return True
                board[i][col] = 0
        return False
    def solveNQ(N, K):
        board = [[0 for j in range(N)] for i in range(N)]
        R = []
        C = []
        for i in range(K):
            r,c = [int(n) for n in input().split()]
            R.append(r)
            C.append(c)
        for i in range(K):
            for j in range(K):
                if i in R and j in C:
                    board[i][j] = 1

        if solveNQUtil(board, 0,N) == False:
            return False

        printSolution(board,N,R,C,K)
        return True
    N,K=[int(n) for n in input().split()]
    solveNQ(N,K)

