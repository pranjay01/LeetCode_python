matrix = [
  []
]
target = 13

def bnrySrch(List,target,low,high):
    mid = int((low+high)/2)
    if low>high:
        return False
    tmp = List[mid]
    if tmp==target:
        return True
    elif target > tmp:
        return bnrySrch(List,target,mid+1,high)
    else:
        return bnrySrch(List,target,low,mid-1)


for List in matrix:
    if not List:
        continue
    if target==List[0] or target==List[-1]:
        print (True)
    elif target>List[0] and target<List[-1]:
        print (bnrySrch(List,target,0,len(List)-1))
    
print (False)