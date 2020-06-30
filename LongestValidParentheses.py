s="()((())()"

length=len(s)
if length==0:
    print (0)
sI=0
subs=''
subl=[]
maxl=0

for i in range(length):
    if s[i]=='(':
        subs=subs+'('
        subl.append(i)
    else:
        if i>0 and subl and subs[-1]=='(':
            subs=subs[:-1]
            subl.pop()
        else:
            tmp = i-sI
            if tmp>maxl:
                maxl=tmp
            sI=i+1
            
if subl:
    prev=i+1
    if sI>=subl[-1]:
        tmp=i-sI
        if tmp>maxl:
            print (tmp)
    
    lengL=len(subl) -1
    index=subl[lengL]
    # if sI==0:
    #     if subl[0]-sI > maxl:
    #         maxl=subl[0]-sI
    while lengL>=0 and sI<=index:
        tmp1=prev-index-1
        tmp2=0
        if sI>index and sI<prev:
            tmp2=prev-sI
        elif sI==prev and sI<index:
            tmp2=index-sI-1
        if tmp1>tmp2 and tmp1>maxl:
            maxl=tmp1
        elif tmp2>tmp1 and tmp2>maxl:
            maxl=tmp2
        prev=index
        lengL-=1
        index=subl[lengL]
    tmp=subl[0]
    if sI<tmp and (tmp-sI>maxl):
        maxl=tmp-sI
        
    print (maxl)
else:
    if (i-sI) > maxl:
        print (i-sI+1)
    else:
        print (maxl)