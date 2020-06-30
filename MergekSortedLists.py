class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers1=[1,3,4]
numbers2=[]
numbers3=[2,6]
dummyRoot1 = ListNode(0)
l1 = dummyRoot1
for number in numbers1:
        l1.next = ListNode(number)
        l1 = l1.next
l1 = dummyRoot1.next

dummyRoot2 = ListNode(0)
l2 = dummyRoot2

for number in numbers2:
        l2.next = ListNode(number)
        l2 = l2.next
l2 = dummyRoot2.next

dummyRoot3 = ListNode(0)
l3 = dummyRoot3
for number in numbers3:
        l3.next = ListNode(number)
        l3 = l3.next
l3 = dummyRoot3.next

lists=[]
lists.append(l1)
lists.append(l2)
lists.append(l3)

def sortedMerge(l, r): 
    result = None
    if not l: 
        return r
    if not r: 
        return l 
            
    if l.val <= r.val: 
        result = l
        result.next = sortedMerge(l.next, r) 
    else: 
        result = r
        result.next = sortedMerge(l, r.next) 
    return result 

def mergeSort(ptr):
    if not ptr or not ptr.next:
        return ptr
    m=getMiddle(ptr)
    ntm=m.next

    
    m.next = None
  
    # Apply mergeSort on left list  
    left = mergeSort(ptr) 
        
    # Apply mergeSort on right list 
    right = mergeSort(ntm) 

    # Merge the left and right lists  
    sortedlist = sortedMerge(left, right) 
    return sortedlist 

def getMiddle(ptr):
    if not ptr:
        return ptr

    left=ptr
    right=ptr

    while right.next and right.next.next:
        left=left.next
        right=right.next.next

    return left

length = len(lists)
ptr=ListNode()

if length==0:
    ptr=None
    print( ptr)

ptr=lists[0]
for index in range(length):
    while ptr and ptr.next:
        ptr=ptr.next
    if ptr and index<length-1:
        ptr.next=lists[index+1]
    elif not ptr and index<length-1:
        ptr = lists[index+1]

for index in range(length):
    if lists[index]:
        ptr=lists[index]
        break



ptr = mergeSort(ptr)
print (ptr)

