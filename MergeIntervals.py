intervals = [[1,5]]
newInterval = [2,7]
#intervals.append(newInterval)
#intervals.sort()
l=len(intervals)

if not intervals and not newInterval:
    print ([])
elif intervals and not newInterval:
    res=[intervals[0]]
    List=0
elif not intervals and newInterval:
    res=[newInterval]
    List=0
else:
    if newInterval<intervals[0]:
        res=[newInterval]
        List=0
    else:
        res=[intervals[0]]
        List=0
        

while List <l:
    if res[-1]<newInterval and newInterval<intervals[List]:
        if newInterval[0]>res[-1][-1]:
            res.append(newInterval)
        elif newInterval[-1]>res[-1][-1]:
            res[-1][-1]=newInterval[-1]
        continue

            
    if intervals[List][0]<=res[-1][-1]:
        if  intervals[List][0]<=res[-1][0]:
            res[-1][0]=intervals[List][0]
        # else:
        #     res[-1][0]=res[-1][0]
        if  intervals[List][-1]>res[-1][-1]:
            res[-1][-1]=intervals[List][-1]
        # else:
        #     res[-1][-1]=intervals[List][-1]
    else:
        res.append(intervals[List])
    
    List+=1

print (res)