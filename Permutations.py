nums=[1,2,3,4]


def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
def devideFact(psblVr,n,k,seq):
    if n==1:
        return seq
    elif n==2:
        if k==1:
            return seq
        else:
            return (seq[1:]+seq[0:1])
    psblVr=int(psblVr/n)
    if k%psblVr==0:
        index=int(k/psblVr)-1
        k=psblVr
    else:
        index=int(k/psblVr)
        k=k%psblVr

    return (seq[index:index+1]+devideFact(psblVr,n-1,k,seq[0:index]+seq[index+1:]))

res=[]
l=len(nums)


total=fact(l)+1
for k in range(1,total):
    res.append(devideFact(total-1,l,k,nums))

print (res)