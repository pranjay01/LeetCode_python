nums = [3,0,0]

iTrack=[]
l=len(nums)
# maxV=0
for i in range(l-1):
    # t=
    if nums[i]==0:
        iTrack.append(i)
    # if t>maxV:
    #     maxV=t

if not iTrack:
    print (True)

for index in iTrack:
    find=False
    i=index-1
    while i>=0 :
        if (i+nums[i])>(index):
            find=True
            break
        i-=1
    if not find:
        print (False)
else:
    print (True)