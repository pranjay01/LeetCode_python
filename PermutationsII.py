nums=[1,1,2,2]


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

nums.sort()
res=set()
l=len(nums)

# if l==0 or l==1:
#     print ([nums])

total=fact(l)+1
track={}
i=0

p=int(total/l)
for k in range(1,total):
    if nums[i] not in track:
        # tmp=devideFact(total-1,l,k,nums)
        # res[''.join(str(tmp))]=tmp
        res.add(tuple(devideFact(total-1,l,k,nums)))
    if (k)%p==0:
        track[nums[i]]=i
        i+=1    
        
#res = list(res.values())
# import itertools
# res.sort()
# res=list(res for res,_ in itertools.groupby(res))
#res = list(set(tuple(sub) for sub in res)) 
res=list(res)
print (res)