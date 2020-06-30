candidates = [2,3,5]
target = 8


if not candidates or candidates[0]>target:
    print ([])

def helper(limit,candidates,target,lst):
    if limit==0 and target>candidates[0]:
        lst.clear()
        return 0
    
         



candidates = candidates.sort()
length = len(candidates)
i=0
result=[]
for i in range(length):
    if candidates[i]>target:
        break
    tmp=[candidates[i]]
    helper(i,candidates,target-candidates[i],tmp)
    if tmp:
        result.append(tmp)

