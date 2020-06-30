class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTree(inputValues):
    #inputValues = [1,2,3]
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

root=getTree([1,'null',2,3])





class Solution:
    def inorderTraversal(self, root: TreeNode):
        res=[]
        if root:
            self.toList(root,res)
        return res


    def toList(self,tree,tlist):
        if tree.left:
            self.toList(tree.left,tlist)
        
        tlist.append(tree.val)

        if tree.right:
            self.toList(tree.right,tlist)
        
        return tlist


print (Solution().inorderTraversal(root))