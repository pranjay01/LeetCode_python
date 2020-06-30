grid=[
 
]
m=len(grid)
if m>0:
    n=len(grid[0])
else:
    print (0)
if n==0:
    

for i in range(1,m):
    grid[i][0] += grid[i-1][0]

for i in range(1,n):
    grid[0][i] += grid[0][i-1]



for i in range (1,m):
    for j in range (1,n):
        if grid[i-1][j]<grid[i][j-1]:
            grid[i][j]+=grid[i-1][j]
        else:
            grid[i][j]+=grid[i][j-1]

print (grid[-1][-1])