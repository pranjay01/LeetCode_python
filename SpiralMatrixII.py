n=0

res=[]
i=0
j=0
while i<n:
    tmp=[]
    res.append(tmp)
    while j<n:
        tmp.append(0)

        j+=1
    j=0
    i+=1
#res=[res]*3

i=0
j=0
co=n*n
m=n
movement='F'
jmin=0
imin=0
limit=1
while limit<=co:
    res[i][j]=limit
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
    limit+=1
print (res)
