def search(nums,target):
    high =len(nums)-1
    low=0
    mid=int((high+low)/2)
    while high>=low:
        midv=nums[mid]
        if target>midv:
            low=mid+1
            mid=int((high+low)/2)
        elif target<midv:
            high=mid-1
            mid=int((high+low)/2)
        else:
            return mid
    return -1
nums = [2,2]
target = 2
l=len(nums)
index=-1
if l>0:
    index = search(nums,target)
if index<0:
    print ([-1,-1])
else:
    #result=[index]
    #find initial
    i=index-1
    while i>=0 and nums[i]==target:
        #result[0]=i
        i-=1
    result=[i+1]
    result.append(index)
    i=index+1
    while i<l and nums[i]==target:
        #result[1]=i
        i+=1
    result[1]=i-1
    print (result)





