nums = [1]
val=1
i=0
length=len(nums)
while i<length:
    if nums[i]==val:
        nums.pop(i)
        length-=1
        #i-=1
    else:
        i+=1
print (length)