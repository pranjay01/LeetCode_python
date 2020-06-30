class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

number=[1,1]

dumyroot = ListNode(0)
head = dumyroot
for num in number:
    head.next=ListNode(num)
    head=head.next
head = dumyroot.next

# if head:
#     ptrf=head.next
# else:
#     print (head)
val=None
if head:
    ptrb=head
else:
    print (head)
while ptrb.next :
    if ptrb.val==ptrb.next.val or ptrb.next.val==val:
        #ptrf=ptrf.next
        ptrb.next=ptrb.next.next
    else:
        #ptrf=ptrf.next
        ptrb=ptrb.next

print (head)