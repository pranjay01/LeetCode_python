obstacleGrid=[
  [0]
]
m=len(obstacleGrid)
if m == 0:
    print (1)
n=len(obstacleGrid[0])
if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
    print (0)

# i=0
# j=0
# while i<m:
#     j=0
#     while j<n:
#         if i==0 or j==0:
#             if obstacleGrid[i][j]==1:
#                 if i==0:
#                     i+=1
#                     break
#                 else:
#                     i=m
#             else:
#                 obstacleGrid[i][j]=1
#         elif obstacleGrid[i][j]==1:
#             obstacleGrid[i][j]=0
#         j+=1
#     i+=1
#obstacleGrid[0][0]
i=0
j=0
while i <m:
    j=0
    while j <n:
        if i==0:
            if obstacleGrid[i][j]==1:
                obstacleGrid[i][j]=0
                while j < n:
                    obstacleGrid[i][j]=0
                    j+=1
                break
            else:
                obstacleGrid[i][j]=1
        elif(j==0):
            if obstacleGrid[i][j]==1 or obstacleGrid[i-1][j]==0:
                obstacleGrid[i][j]=0
            else:
                obstacleGrid[i][j]=1

        else:
            if obstacleGrid[i][j]==1:
                obstacleGrid[i][j]=0
            else:
                obstacleGrid[i][j]=1
        j+=1
    i+=1
for i in range(1,m):
    for j in range(1,n):
        if not obstacleGrid[i][j]==0: 
            obstacleGrid[i][j]=obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

print (obstacleGrid[m-1][n-1])
