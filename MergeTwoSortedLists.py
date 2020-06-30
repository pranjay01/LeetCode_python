class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers1=[1,2,4]
numbers2=[1,3,4,5]
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


dummyRoot = ListNode(0)
ptr = dummyRoot
ptr1=ListNode()
ptr1=ListNode()
ptr1=l1
ptr2=l2

while ptr1 and ptr2:
    if ptr1.val<ptr2.val:
        ptr.next=ListNode(ptr1.val)
        ptr=ptr.next
        ptr1=ptr1.next
    elif ptr1.val>ptr2.val:
        ptr.next=ListNode(ptr2.val)
        ptr=ptr.next
        ptr2=ptr2.next
    else:
        ptr.next=ListNode(ptr1.val)
        ptr=ptr.next
        ptr.next=ListNode(ptr2.val)
        ptr=ptr.next
        ptr1=ptr1.next
        ptr2=ptr2.next
if ptr1 and not ptr2:
    ptr.next=ptr1
elif ptr2 and not ptr1:
    ptr.next=ptr2



ptr = dummyRoot.next
print (ptr)