n = 2

i=0
initial='1'
while i<n-1:
    tmp=""
    count=0
    st=initial[0]
    tmplen=len(initial)
    tmpval=''
    for j in  range(0,tmplen):
        tmpval=initial[j]
        if tmpval==st:
            count+=1
        else:
            tmp=tmp+str(count)+initial[j-1]
            count=1
            st=tmpval
    tmp=tmp+str(count)+tmpval
    initial=tmp
    i+=1
    #print (initial)        

print (initial)    