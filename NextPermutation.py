nums= [1,3,2]

length = len(nums)
psbl=False

for i in range(length-1):
    if nums[i]<nums[i+1]:
        psbl=True
        index=i
        j=i+1
        while j<length-1:
            if nums[j]<nums[j+1]:
                index=j
            j+=1

        
    
        s=nums[index]
        m=nums[index+1]
        jindex=index+1
        for j in range(index+1,length):
            l=nums[j]
            if l>s and l<m:
                m=l
                jindex=j
        nums[jindex]=s
        nums[index]=m
        nums[index+1:]=sorted(nums[index+1:])            
        break

if not psbl:
    nums.sort()

print(nums)