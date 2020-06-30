n=5
k=15

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
            return (seq[1]+seq[0])
    psblVr=int(psblVr/n)
    if k%psblVr==0:
        index=int(k/psblVr)-1
        k=psblVr
    else:
        index=int(k/psblVr)
        k=k%psblVr

    return (seq[index]+devideFact(psblVr,n-1,k,seq[0:index]+seq[index+1:]))

seq=''
for i in range(1,n+1):
    seq=seq+str(i)
res=''+devideFact(fact(n),n,k,seq)

print (res)