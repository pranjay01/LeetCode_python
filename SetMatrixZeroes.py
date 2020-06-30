matrix = [[3,7,2,8,2],[2,2,4,1,8],[0,5,7,6,3],[8,1,0,7,7],[1,3,7,4,1],[6,5,5,6,3],[7,1,0,1,9],[5,4,4,9,7],[2,2,4,1,0],[7,1,1,9,1],[8,0,4,7,6],[7,5,1,2,3],[7,2,5,9,3]]

seq={}
m=len(matrix)
if m>0:
    n=len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                seq['i' + str(i)]=None
                seq['j' + str(j)]=None
                #seq=seq + 'i' + str(i) + ' ' + 'j' + str(j) + ' '

    if seq:
        for i in range(m):
            for j in range(n):
                if (('i' + str(i)) in seq) or (('j' + str(j)) in seq):
                    matrix[i][j]=0


print (matrix)