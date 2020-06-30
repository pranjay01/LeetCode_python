matrix=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

m=len(matrix)
if m==0:
    print ([])
n=len(matrix[0])
i=0
j=0
co=0
res=[]
movement='F'
jmin=0
imin=0
limit=m*n
while co<limit:
    res.append(matrix[i][j])
    if movement=='F':
        j=j+1
        if j==n:
            j-=1
            i+=1
            movement='D'
            imin+=1
            
    elif movement=='D':
        i+=1
        if i==m:
            i-=1
            n-=1
            j-=1
            movement='B'
            
    elif movement=='B':
        j-=1
        if j<jmin:
            j=jmin
            m-=1
            i-=1
            movement='U'
    elif movement=='U':
        i-=1
        if i<imin:
            i=imin
            jmin+=1
            j+=1
            movement='F'
    co+=1
print (res)
