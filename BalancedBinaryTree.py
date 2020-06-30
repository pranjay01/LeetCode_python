class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTree(inputValues):
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

    return (root)
root=getTree([1,2])


class Solution:
    def isBalanced(self, root: TreeNode) -> int:
        b=[True]
        self.check(root,b)
        return b[0]

    def check(self,root,b):
        if root:
            if root.left is None and root.right is None:
                return 1
            left=0
            right=0
            if root.left:
                left = 1 + self.check(root.left,b)
           
            if root.right:
                right = 1 + self.check(root.right,b)
            
            if abs(left-right)>1:
                if left==0 or right ==0:
                    if abs(left-right)>2:
                        b[0]=False
                else:
                    b[0]=False
            return max(left,right)
        else:
            return 0

print (Solution().isBalanced(root))