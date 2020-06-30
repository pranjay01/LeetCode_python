nums = [0,0,0,0]
target =0

def threesum(nums, target: int,resultset,val:int):
    length  = len(nums)
    for i1 in range(length-2):
        i2=i1+1
        i3=length-1
        num1=nums[i1]
        tar=target-num1
        num2=nums[i2]
        num3=nums[i3]
        while i2<i3:
            pair=num2+num3
            if pair>tar:
                i3-=1
                num3=nums[i3]
            elif pair<tar:
                i2+=1
                num2=nums[i2]
            else:
                resultset.add((val,num1,num2,num3))
                i2+=1
                i3-=1
                num2=nums[i2]
                num3=nums[i3]
    return resultset

result=[]
resultset=set()
nums.sort()
length = len(nums)
if nums.count(0)>=4 and target==0:
    resultset.add((0,0,0,0))
for index in range(length-3):
    val=nums[index]
    resultset=threesum(nums[index+1:],target-val,resultset,val)

resultset = list(resultset)
for t in resultset:
    result.append(list(t))
print (result)