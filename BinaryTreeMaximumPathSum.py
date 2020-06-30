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
root=getTree([1,2,3])


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left=self.maxPathSum(root.left)
        right=(self.maxPathSum(root.right))

        maxv=max(left+right+root.val, self.maxPathSum(root.left),self.maxPathSum(root.right)) 

        return maxv

print(Solution().maxPathSum(root))