word1 = "intention"
word2 = "execution"

if word1==word2:
    print(0)

m1=len(word1)+1
n=len(word2)+1

grid1=[]
grid2=[]
for i in range(m1):
    grid1.append(i)
   
for i in range (1,n):
    for j in range(m1):
        if j==0:
            grid2.append(i)
            continue
        if word1[j-1]==word2[i-1]:
            grid2.append(grid1[j-1])
        else:
            grid2.append(1+min(grid2[j-1], grid1[j], grid1[j-1]))
    grid1=grid2
    grid2=[]

print (grid1[-1])
