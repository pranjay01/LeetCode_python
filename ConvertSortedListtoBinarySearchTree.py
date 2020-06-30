class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
numbers=[0,1,2,3,4,5]
dummyRoot = ListNode(0)
head = dummyRoot
for number in numbers:
        head.next = ListNode(number)
        head = head.next
head = dummyRoot.next
class Solution:
    def sortedArrayToBST(self, head) -> TreeNode:
        l=999999
        return self.toTree(head,l)
        
    def toTree(self,head,l):
        prev=None
        ptr1=head
        ptr2=head
        count=1
        while ptr2.next and count<l:
            prev=ptr1
            ptr1=ptr1.next

            ptr2=ptr2.next
            count+=1
            if ptr2.next and count<l:
                ptr2=ptr2.next
                count+=1
        node=TreeNode(ptr1.val)

        if prev:
            node.left=self.toTree(head,int(count/2))
        r=count - int(count/2)-1
        if ptr1.next and r>0:
            node.right=self.toTree(ptr1.next,r)

        return node

#nums=[-10,-3,0,5,9]

print (Solution().sortedArrayToBST(head))
#print (nums)