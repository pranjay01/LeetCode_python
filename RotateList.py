class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers1=[0,1,2]
#numbers2=[1,3,4,5]
dummyRoot1 = ListNode(0)
head = dummyRoot1
for number in numbers1:
        head.next = ListNode(number)
        head = head.next
head = dummyRoot1.next
k=4
start=head
last=head
prev=None



leng=1



while last.next:
        leng+=1
        prev=last
        last=last.next

k=k%leng

while k > 0:
        last.next=start
        start=last
        last=prev
        last.next=None
        prev=start
        while prev.next is not last:
                prev=prev.next
        k-=1

print (start)