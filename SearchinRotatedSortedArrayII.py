nums = [1,1]
target = 0

if not nums:
    print (False)

l=len(nums)

while l>1 and nums[0]==nums[-1]:
    nums.pop()
    l-=1

temp = min(nums) 
index = nums.index(temp)

def search(nums,target,index,l_r,l):
    if l_r=='l':
        high =index
        low=0
        mid=int(high/2)
    else:
        high =l
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
            return True
    return False
if target==temp:
    print (True)
elif target>nums[-1]:
    if target<nums[0]:
        print (False)
    print (search(nums,target,index,'l',l))
elif target<nums[-1]:
    print (search(nums,target,index,'r',l))
else:
    print (True)


