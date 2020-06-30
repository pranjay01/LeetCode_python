class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers1=[1,2,3,4,5,6]
#numbers2=[1,3,4,5]
dummyRoot1 = ListNode(0)
head = dummyRoot1
for number in numbers1:
        head.next = ListNode(number)
        head = head.next
head = dummyRoot1.next
k=6

dummyRoot = ListNode(0)
result = dummyRoot
result.next=head
ptr1=head
ptr2=head
prev=None
next=None
n=1
i=0
while n<=k and ptr1:
    n+=1
    ptr1=ptr1.next
    if n==k and ptr1:
        
        prev=ptr1.next
        while i<k:
            i+=1
            next=ptr2.next
            ptr2.next=prev
            prev=ptr2
            ptr2=next
        result.next=prev
        i=0
        while result.next and i<k:
            i+=1
            result=result.next
        ptr1=ptr2
        i=0
        n=1
    
        
print (dummyRoot.next)