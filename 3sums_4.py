nums = [0]
import time
tic = time.perf_counter()

result=[]
resultset=set()
nums.sort()
length  = len(nums)
if length ==0:
    print ([])
if nums[0]>0 or nums[-1]<0:
    print ([])
if nums[-1]==0:
    if nums.count(0)>=3:
        print ([[0,0,0]])
    else:
        print ([])
if nums.count(0)>=3:
    resultset.add((0,0,0))
postiveindex=next(x[0] for x in enumerate(nums) if x[1] > 0)
for i1 in range(postiveindex):
    i2=i1+1
    i3=length-1
    num1=nums[i1]
    target=-1*num1
    num2=nums[i2]
    num3=nums[i3]
    while i2<i3:
        pair=num2+num3
        if pair>target:
            i3-=1
            num3=nums[i3]
        elif pair<target:
            i2+=1
            num2=nums[i2]
        else:
            resultset.add((num1,num2,num3))
            i2+=1
            i3-=1
            num2=nums[i2]
            num3=nums[i3]

resultset = list(resultset)
for t in resultset:
    result.append(list(t))
print (result)
toc = time.perf_counter()
#print (mid-tic)
print (toc-tic)
