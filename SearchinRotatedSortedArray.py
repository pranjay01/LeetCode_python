nums = [1]
if not nums:
    print (-1)
target=2
temp = min(nums) 
index = nums.index(temp)

def search(nums,target,index,l_r):
    if l_r=='l':
        high =index
        low=0
        mid=int(high/2)
    else:
        high =len(nums)
        low=index
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
if target==temp:
    print (index)
elif target>nums[-1]:
    if target<nums[0]:
        print (-1)
    print (search(nums,target,index,'l'))
elif target<nums[-1]:
    print (search(nums,target,index,'r'))
else:
    print (len(nums)-1)


