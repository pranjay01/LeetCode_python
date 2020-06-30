class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers=[1,2,3,4,5]
dummyRoot = ListNode(0)
head = dummyRoot
for number in numbers:
        head.next = ListNode(number)
        head = head.next
head = dummyRoot.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dumy=ListNode(0)
        dumy.next=head
        curr = dumy
        prev=None
        nextn=None
        i=0
        while curr:
            if i==(m-1):
                front=curr    
                curr=curr.next
                front.next=None
                tail=curr            
            elif i>=m and i<=n:
                nextn=curr.next
                curr.next=prev
                prev=curr
                curr=nextn
            elif i>n:
                break
            else:
                curr=curr.next
            i+=1
        front.next=prev
        tail.next=curr
        if m==1:
            return front.next
        return head
m=1
n=4
node = Solution().reverseBetween(head,m,n)

print (node)
