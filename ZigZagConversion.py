s =""
numRows=4
length = len(s)

if numRows>=length or numRows==1:
    print (s)
front = (numRows-1)*2 
back = 0
res=""
i=0
while i<numRows:
    tmp=i
    res = res + s[tmp]

    while tmp<length:
        tmp = tmp+front
        if front > 0 and tmp<length:
            res=res + s[tmp]
        tmp = tmp+back
        if back > 0 and tmp<length:  
            res=res + s[tmp]
    i=i+1
    front = front-2
    back=back+2

print(res)
        

