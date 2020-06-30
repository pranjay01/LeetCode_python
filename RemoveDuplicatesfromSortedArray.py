nums = [1,1,2]

i=0
length=len(nums)
while i<length-1:
    if nums[i]==nums[i+1]:
        nums.pop(i+1)
        length-=1
    else:
        i+=1
print (nums)