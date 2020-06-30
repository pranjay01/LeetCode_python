def validSudoku(board):
    cllist=['a','a','a','a','a','a','a','a','a']
    for i in range (0,9):
        r={}
        for j in range (0,9):
            
            tmp1=board[i][j]
            tmp2=cllist[j]

            if tmp1 is not '.':
                if (tmp1 not in tmp2):
                    cllist[j] = tmp2 + tmp1
                else:
                    return (False)
                

                if tmp1 in r:
                    return (False)
                else:
                    r[tmp1]=True
            if i%3==1 and j%3==1:
                tmp1=i-1
                tmp2=j-1
                blk='a'
                for k in range (tmp1,tmp1+3):
                    for l in range (tmp2,tmp2+3):
                        tmp = board[k][l]
                        if tmp is not '.' and tmp in blk:
                            return (False)
                        else:
                            blk=blk+ board[k][l]

    return (True)

def columnCheck(board,i):
    blk='a'
    for j in range (0,9):
        tmp=board[i][j]
        if tmp is not '.'and tmp in blk:
            return
        else:
            blk=blk+tmp
    return True
def rowCheck(board,j):
    blk='a'
    for i in range (0,9):
        tmp=board[i][j]
        if tmp is not '.'and tmp in blk:
            return
        else:
            blk=blk+tmp
    return True
def blockCheck(board,i,j):
    i=i-i%3
    j=j-j%3
    blk='a'
    for k in range (i,i+3):
        for l in range (j,j+3):
            tmp = board[k][l]
            if tmp is not '.' and tmp in blk:
                return (False)
            else:
                blk=blk+ board[k][l]
    return True

board=[[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]

i=0
j=0
track={}

check=True

while True:
    tmp=str(i)+str(j)
    tmp1=board[i][j]
    if tmp not in track:
        if tmp1 is '.':
            board[i][j]='0'
            tmp1='0'
            track[tmp]=True
        else:
            track[tmp]=False
    trackCheck=track[tmp]
    if trackCheck:
        if not check and tmp1=='9':
            board[i][j]='.'
            tmp1='.'
            j-=1
            if j<0:
                j=8
                i-=1
            continue
        if tmp1=='.':    
            board[i][j]='0'
            tmp1='0'
        board[i][j]=str(int(tmp1)+1)
        tmp1=str(int(tmp1)+1)
        check = columnCheck(board,i)
        if check:
            check=rowCheck(board,j)
        if check:
            check=blockCheck(board,i,j)




    if check:
        if i==8 and j==8:
            print (board)
            break
        else:
            j+=1
            if j==9:
                i+=1
                j=0
    else:
        if trackCheck and tmp1=='9':
            board[i][j]='.'
            #tmp1='.'
            j-=1
            if j<0:
                j=8
                i-=1
        if not trackCheck:
            j-=1
            if j<0:
                j=8
                i-=1