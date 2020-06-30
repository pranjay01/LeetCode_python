matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

def maxArea(heights):
    while heights[-1]==0:
        heights.pop()
    heights.append(0)
    stackList1=[]
    l=len(heights)
    maxa=0
    for i in range(l):
        if stackList1:
            tmp=stackList1[-1][1]
            if heights[i]>=tmp:
                stackList1.append((i,heights[i]))
            else:
                #k=1
                if tmp>maxa:
                    maxa=stackList1[-1][1]
                t=stackList1[-1][0]
                tmp3=(i-t+1)*heights[i]
                if tmp3>maxa:
                    maxa=tmp3
                stackList1.pop()
                while stackList1 and stackList1[-1][1]>heights[i]:
                    tmp2=stackList1[-1]
                    if tmp2[1]<tmp:
                        tmp=tmp2[1]
                    tmp3=(i-tmp2[0])*tmp
                    if tmp3>maxa:
                        maxa=tmp3
                    t=stackList1[-1][0]
                    stackList1.pop()
                # if stackList1:
                #     stackList1.append((i,heights[i]))
                # else:
                stackList1.append((t,heights[i]))

        else:
            stackList1.append((i,heights[i]))
    return (maxa)

m=len(matrix)
if m==0:
    print (0)
else:
    n=len(matrix[0])

if n==0:
    print (0)
res=0
for i in range(m):
    for j in range(n):
        if i==0:
            matrix[i][j]=int(matrix[i][j])
        elif matrix[i][j]=='0':
            matrix[i][j]=int(matrix[i][j])
            continue
        else:
            matrix[i][j]=int(matrix[i][j])+int(matrix[i-1][j])
    print(matrix[i])
    res=max(res,maxArea(matrix[i]))

print (res)