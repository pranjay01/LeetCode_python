board=[["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]

cllist=['a','a','a','a','a','a','a','a','a']
for i in range (0,9):
    r={}
    for j in range (0,9):
        if i%3==1 and j%3==1:
            tmp1=i-1
            tmp2=j-1
            blk='a'
            for k in range (tmp1,tmp1+3):
                for l in range (tmp2,tmp2+3):
                    tmp = board[k][l]
                    if tmp is not '.' and tmp in blk:
                        print (False)
                    else:
                        blk=blk+ board[k][l]


        tmp1=board[i][j]
        tmp2=cllist[j]

        if tmp1 is not '.':
            if (tmp1 not in tmp2):
                cllist[j] = tmp2 + tmp1
            else:
                print (False)
            

            if tmp1 in r:
                print (False)
            else:
                r[tmp1]=True

print (True)
