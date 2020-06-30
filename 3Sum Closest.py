nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]

target = 0
import time
tic = time.perf_counter()

nums.sort()
length  = len(nums)


num1=nums[0]
num2=nums[1]
num3=nums[-1]
sum=num1+num2+num3
dfrnce=sum-target
if dfrnce<0:
    dfrnce=-1*dfrnce
elif dfrnce==0:
    print (sum)
prevdfrnce=dfrnce
# i2=2
# num2=nums[i2]
for i1 in range(len(nums)):
    if i1 >= length-2:
        break
    num1=nums[i1]
    # if i1>0:
    i2=i1+1
    num2=nums[i2]
    i3=length-1
    num3=nums[i3]

    while i2<i3:
        currdfrnce=num1+num2+num3-target
        if currdfrnce<0:
            currdfrnce=-1*currdfrnce

            if currdfrnce>prevdfrnce:
                i2 = i2+1
                i3 -=1
                num2=nums[i2]
                num3=nums[i3]
                prevdfrnce=currdfrnce
            else :
                if currdfrnce<dfrnce:
                    dfrnce=currdfrnce
                    sum=num1+num2+num3
                    if dfrnce==0:
                        print (sum)
                prevdfrnce=currdfrnce
                i2+=1
                num2=nums[i2]
            
        elif currdfrnce>0:
            if currdfrnce<prevdfrnce:
                if currdfrnce<dfrnce:
                    dfrnce=currdfrnce
                    sum=num1+num2+num3
                    if dfrnce==0:
                        print (sum)
            prevdfrnce=currdfrnce
            i3-=1
            num3=nums[i3]
            
        else:
            print (num1+num2+num3)

print (sum)