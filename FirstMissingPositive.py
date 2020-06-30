nums = [1,1000,5]


if not nums:
    print (1)

nums=list(set(nums))
nums.sort()
if nums[0]>0:
    c=1
    for n in nums:
        if n==c:
            c+=1
        else:
            print (c)
    print (c)
else:
    c=1
    for n in nums:
        if n>0:
            if n==c:
                c+=1
            else:
                print (c)
    print (c)