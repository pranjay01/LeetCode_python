nums = [0,0,1,1,1,1,2,3,3]

count=0
l=len(nums)
if l==0 or l==1:
    print (l)
i=1

while i<l:
    if nums[i]==nums[i-1]:
        if count < 2:
            count=2
            i+=1
            continue
        else:
            nums.pop(i)
            l-=1
            continue
    else:
        count=0
        i+=1

print (l)

print (nums)