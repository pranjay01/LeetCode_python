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
root=getTree([])

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            nodeq=[]
            self.NodeInList(root,nodeq)
            nodeq=nodeq[1:]
            ptr=root
            ptr.left=None
            ptr.right=None
            for node in nodeq:
                ptr.right=node
                ptr.left=None
                ptr=ptr.right
        
        #print(root)

    def NodeInList(self,root,nodeq):
        if root:
            nodeq.append(root)
        
        if root.left:
            self.NodeInList(root.left,nodeq)

        if root.right:
            self.NodeInList(root.right,nodeq)


Solution().flatten(root)