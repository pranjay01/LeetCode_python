class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        if m>0:
            n=len(board[0])
        else:
            return 0
        
        #m-=1
        #n-=1

        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1:
                    if board[i][j]=='O':
                        self.check(i,j,board,m,n)
                else:
                    if j==0 or j==n-1:
                        if board[i][j]=='O':
                            self.check(i,j,board,m,n)
        m-=1
        n-=1
        for i in range(1,m):
            for j in range(1,n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='.':
                    board[i][j]='O'
        
    def check(self,i,j,board,m,n):
        if (i==0 or i==m-1) and (j==0 or j==n-1):
            return 0
        if i==0:
            if board[i+1][j]=='O':
                board[i+1][j]='.'
                self.check(i+1,j,board,m,n)
        elif i==m-1 :
            if board[i-1][j]=='O':
                board[i-1][j]='.'
                self.check(i-1,j,board,m,n)
        elif j==0 :
            if board[i][j+1]=='O':
                board[i][j+1]='.'
                self.check(i,j+1,board,m,n)
        elif j==n-1 :
            if board[i][j-1]=='O':
                board[i][j-1]='.'
                self.check(i,j-1,board,m,n)
        elif(not(i==0 or i==m-1) and not(j==0 or j==n-1)):
            if i-1>0 and board[i-1][j]=='O':
                board[i-1][j]='.'
                self.check(i-1,j,board,m,n)
            if i+1 < m-1 and board[i+1][j]=='O':
                board[i+1][j]='.'
                self.check(i+1,j,board,m,n)
            if j-1>0 and board[i][j-1]=='O':
                board[i][j-1]='.'
                self.check(i,j-1,board,m,n)
            if j+1<n-1 and board[i][j+1]=='O':
                board[i][j+1]='.'
                self.check(i,j+1,board,m,n)
        

board=[
["O","X","O","O","O","X"],
["O","O","X","X","X","O"],
["X","X","X","X","X","O"],
["O","O","O","O","X","X"],
["X","X","O","O","X","O"],
["O","O","X","X","X","X"]]

Solution().solve(board)
print(board)