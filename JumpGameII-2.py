nums=[2,1]


def findindexOfMax(nums,start,limit,l):
    
    if limit>l:
        return l
    bigv=nums[start]
    index=start
    for i in range(start,limit):
        tmp=nums[i]
        if ((i+tmp)>=bigv+index):
                index=i
                bigv=tmp
            # else:
            #     index=limit-1
        
    return index

l=len(nums)

if l==1:
    print (0)
curr=0
maxd=nums[curr]
count=1
while curr<l-1:
    
    curr=findindexOfMax(nums,curr+1,maxd+curr+1,l-1)
    if curr==(l-1):
        break
    count+=1
    maxd=nums[curr]
    
print (count)
