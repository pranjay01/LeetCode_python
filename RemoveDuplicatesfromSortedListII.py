class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

number=[-3,-1,0,3]

dumyroot = ListNode(0)
head = dumyroot

for num in number:
    head.next=ListNode(num)
    head=head.next

head = dumyroot.next

print (head)

heaD=False
if head:
    if head.next and head.val==head.next.val:
        heaD=True
        while head.next and head.val==head.next.val:
            head=head.next
        
    ptrf=head.next
else:
    print (head)
val=None

ptrb=head


while ptrf :
    if ptrf.next and ptrf.val==ptrf.next.val:
        val=ptrf.val
        ptrf=ptrf.next.next
        ptrb.next=ptrf
        if head.val==val:
            head=ptrb
    elif ptrf and ptrf.val==val:
        ptrf=ptrf.next
        ptrb.next=ptrf
        if head.val==val:
            head=ptrb
    else:
        ptrf=ptrf.next
        ptrb=ptrb.next

# if head.next and head.val==head.next.val:
#     ptrb=head
#     ptrf=head.next

if heaD:
    print (head.next)
print (head)