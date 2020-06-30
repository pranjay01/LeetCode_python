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
root=getTree([-2,'null',-3])

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        b=[False]
        if root:
            self.check(root,sum,b)
            return b[0]
        else:
            return False
        
    def check(self,root,sum,b):
        if b[0]:
            return True
        if root:
            sum=sum-root.val
        if sum==0 and not root.left and not root.right:
            b[0]=True
        if root.left:
            self.check(root.left,sum,b)

        if root.right:
            self.check(root.right,sum,b)


print(Solution().hasPathSum(root,-5))