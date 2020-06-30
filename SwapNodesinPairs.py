class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers1=[1,2,3,4,5]
#numbers2=[1,3,4,5]
dummyRoot1 = ListNode(0)
head = dummyRoot1
for number in numbers1:
        head.next = ListNode(number)
        head = head.next
head = dummyRoot1.next


if not head or not head.next:
    print (head)

dummyRoot = ListNode(0)
result = dummyRoot
result.next=head
ptr1=head
ptr2=head.next
while ptr1 and ptr2:
    tmp=ptr1
    if ptr2.next:
        ptr1.next=ptr2.next
        ptr2.next=tmp
    else:
        ptr1=ptr2
        ptr2.next=tmp
        ptr2=ptr2.next
        ptr2.next=None
        result.next=ptr1
        break
    
    result.next=ptr2
    result=result.next
    result=result.next
    if ptr1.next:
        ptr1=ptr1.next
    if ptr1.next:
        ptr2=ptr1.next
    else:
        break
    
print (dummyRoot.next)
