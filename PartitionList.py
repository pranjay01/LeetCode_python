class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

numbers=[5]

dumyroot = ListNode(0)
head=dumyroot

for num in numbers:
    head.next=ListNode(num)
    head=head.next

head=dumyroot.next
x=4


ptr1=head
prev=ListNode(0)
prev.next=ptr1
pivot=None
h=False
while ptr1:
    if not pivot and ptr1.val>=x:
        pivot = prev
        if head==ptr1:
            head=pivot
            h=True
        ptr1=ptr1.next
        prev=prev.next
        continue
    if pivot and ptr1.val<x:
        prev.next=ptr1.next
        ptr1.next=pivot.next
        pivot.next=ptr1
        pivot=pivot.next
        ptr1=prev.next
        continue
    ptr1=ptr1.next
    prev=prev.next

if h:
    print (head.next)
print (head)
