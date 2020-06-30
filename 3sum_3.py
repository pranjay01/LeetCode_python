nums = [-5,1,-3,-1,-4,-2,4,-1,-1]
import time
tic = time.perf_counter()
def search(l: int,h: int,nums,srch_no: int) -> int:
    while l<=h:
        mid = int((l+h)/2)
        midval=nums[mid]
        if midval>srch_no:
            h=mid-1
        elif midval<srch_no:
            l=mid+1
        else:
            return mid
    return -1
result=[]
resultset=set()
nums.sort()
length  = len(nums)
if length ==0:
    print ([])
if nums[0]>0 or nums[-1]<0:
    print ([])

zeroindex = search(0,length-1,nums,0)

if zeroindex>0:
    if nums.count(0)>=3:
        resultset.add((0,0,0))
    for i in range(zeroindex):
        nvvum=nums[i]
        psnum=-1*nvvum
        pindex=search(zeroindex+1,length-1,nums,psnum)
        if pindex>0:
            #tmp=(nvvum,0,psnum)
            resultset.add((nvvum,0,psnum))
            # if (tmp not in result):
            #     result.append(tmp)
                #resultset.add(tmp)
    
    for i in range(zeroindex):
        num1=nums[i]
        for j in range(zeroindex+1,length):
            
            num2=nums[j]
            num=num1+num2
            if num<0:
                psnum=num*-1
                pindex=search(zeroindex+1,j-1,nums,psnum)
                if pindex>0:
                    #tmp=(num1,psnum,num2)
                    resultset.add((num1,psnum,num2))
                    # if (tmp not in result):
                    #     result.append(tmp)
                    #resultset.add(tmp)
            elif num>0:
                psnum=num*-1
                pindex=search(i+1,zeroindex,nums,psnum)
                if pindex>0:
                    #tmp=(num1,psnum,num2)
                    resultset.add((num1,psnum,num2))
                    # if (tmp not in result):
                    #     result.append(tmp)
                    #resultset.add(tmp)
elif zeroindex<0:

    postiveindex=next(x[0] for x in enumerate(nums) if x[1] > 0)
    # nums1=nums[:postiveindex]
    # nums2=nums[postiveindex:]
    # n1_len=len(nums1)
    # n2_len=len(nums2)
    #mid = time.perf_counter()
    
    smalnv=nums[postiveindex-1]
    smalpsv=nums[postiveindex]
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
            
        # for j in range(postiveindex,length):
        #     num1=nums[i]
        #     num2=nums[j]
        #     num=num1+num2
        #     if num<0:
        #         psnum=num*-1
        #         jprev=postiveindexpostiveindex[j-1]
                
        #         if not (psnum>jprev or psnum<smalpsv):
                
        #             pindex=search(postiveindex,j-1,nums,psnum)
                    
        #             if pindex>0:
        #                 #tmp=(num1,psnum,num2)
        #                 resultset.add((num1,psnum,num2))
                    
        #     elif num>0:
                
        #         psnum=num*-1
        #         afti=nums[i+1]
                
        #         if not (psnum<afti or psnum>smalnv):
                
        #             pindex=search(i+1,postiveindex-1,nums,psnum)
                    
        #             if pindex>0:
        #                 resultset.add((num1,psnum,num2))
                        

resultset = list(resultset)
for t in resultset:
    result.append(list(t))
print (result)
toc = time.perf_counter()
#print (mid-tic)
print (toc-tic)
