matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]


l =len(matrix)

for i in range(l-1):
    x=l-1-i
    for j in range(l-1-i):
        tmp=matrix[i][j]
        matrix[i][j]=matrix[i+x][j+x]
        matrix[i+x][j+x]=tmp
        x-=1

for i in range(int(l/2)):
    for j in range(l):
        tmp=matrix[i][j]
        matrix[i][j]=matrix[l-i-1][j]
        matrix[l-i-1][j]=tmp


print(matrix) 
