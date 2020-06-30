
nums=[3,3]
target=6

for i in nums[0:]:
    index = nums.index(i)+1
    for j in nums[index:]:
        if ((i+j==target)):
            #result.append(index-1)
            #result.append(nums.index(j,index))
            print( [index-1,nums.index(j,index)])