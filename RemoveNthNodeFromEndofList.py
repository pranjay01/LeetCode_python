class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers=[1,2]
dummyRoot = ListNode(0)
head = dummyRoot
for number in numbers:
        head.next = ListNode(number)
        head = head.next
head = dummyRoot.next
print (head)
ptr=ListNode()
ptr=head
prev=ListNode()
prev=head
count=0
n=2
while ptr.next:
    count+=1
    ptr=ptr.next
    if count>n:
        prev=prev.next
        
if n==1:
    if count==0:
        head=None
    else:
        prev.next=None
if n==2 and count==1:
    head=ptr
    return head
else:
    ptr=prev
    if ptr.next:
        ptr=ptr.next
    if ptr.next:
        ptr=ptr.next
    prev.next=ptr
print (head)
