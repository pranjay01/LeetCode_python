class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        
        l=len(nums)
        if l ==0:
            return None
        mid=int(l/2)
        node=TreeNode(nums[mid])

        if mid-1>=0:
            node.left=self.sortedArrayToBST(nums[0:mid])
        if mid+1<l:
            node.right=self.sortedArrayToBST(nums[mid+1:])

        return node

nums=[-10,-3]

print (Solution().sortedArrayToBST(nums))
print (nums)