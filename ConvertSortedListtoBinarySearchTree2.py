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
        nums=[]
        if head:
            self.toList(head,nums)
            return self.toTree(nums)
        return None
    def toList(self,head,nums):
        while head:
            nums.append(head.val)
            head=head.next
    def toTree(self,nums):
        l=len(nums)
        if l ==0:
            return None
        mid=int(l/2)
        node=TreeNode(nums[mid])

        if mid-1>=0:
            node.left=self.toTree(nums[0:mid])
        if mid+1<l:
            node.right=self.toTree(nums[mid+1:])

        return node

#nums=[-10,-3]

print (Solution().sortedArrayToBST(head))
#print (nums)