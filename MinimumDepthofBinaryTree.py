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
root=getTree([1,2,2,3,3,'null','null',4,4])


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            if root.left is None and root.right is None:
                return 1
            left=0
            right=0
            if root.left:
                left = 1 + self.minDepth(root.left)
           
            if root.right:
                right = 1 + self.minDepth(root.right)
            
            if left==0:
                return right
            if right==0:
                return left
            return max(left,right)
        else:
            return 0

print (Solution().minDepth(root))