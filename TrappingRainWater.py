height = [0,1,0,2,1,0,1,3,2,1,2,1]

def findIndex(nums,h):
    for i in range(len(nums)):
        if nums[i]>=h:
            return i
    return -1


if not height:
    print (0)
l=len(height)

for i in range (l):
    if height[i]>0:
        height=height[i:]
        break
l=l-i-1



w=0
tmp = height[0]
start=0
i=0
while i< l:
    end=findIndex(height[i+1:],tmp)
    #end=end+i+1
    if end>=0:
        end=end+i+1
        i=end
        start+=1
        while start<i:
            w=w+tmp-height[start]
            start+=1
        start=i
        tmp=height[i]
    else:
        height=height[i:]
        height.reverse()
        l=l-i
        i=0
        tmp=height[0]
        start=0


print (w)