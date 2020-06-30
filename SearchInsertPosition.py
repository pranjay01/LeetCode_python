nums=[1]
target=1

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

if not nums:
    print (0)
if target>nums[-1]:
    print (len(nums))

result = search(nums,target)
if result >= 0:
    print (result)
else:
    index = [i for i, j in enumerate(nums) if j > target] 
    print (index[0])