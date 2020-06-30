nums=[1,2,1,1,1]

def findindexOfMax(nums,cur,maxD,l):
    #l=len(nums)-1
    limit=cur+maxD-1
    if limit==(l):
        return (l)
    elif limit>(l):
        limit=l
    maxv=nums[cur]
    index=cur
    for i in range(cur,limit):
        if maxv<nums[i]:
            maxv=nums[i]
            index=i
    return index

l=len(nums)

if l==1:
    print (0)

maxD=nums[0]
count=0
cur=0
while l-cur>maxD and cur<l-1:
    count+=1
    cur=findindexOfMax(nums,cur+1,maxD,l-1)
    maxD=nums[cur]

if l-cur<=maxD and cur<l-1:
    count+=1

print (count)