nums=[-2,1,-3,4,-1,2,1,-5,4]

if not nums:
    print (None)
else:
    maxV=nums[0]

st=0
en=0
Tsum=0

for num in nums:
    Tsum=Tsum+num
    if maxV<Tsum:
        maxV=Tsum
    
    if Tsum<0:
        Tsum=0
    
print (maxV)
