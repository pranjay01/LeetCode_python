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

p=getTree([1,'null',2])
q=getTree([1,"null",2])


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ar1=[]
        ar2=[]
        self.toArray(p,ar1)
        self.toArray(q,ar2)
        
        return ar1==ar2

    def toArray(self,tree,arr):
        if not tree:
            return arr
        arr.append(tree.val)

        if tree.left:
            self.toArray(tree.left,arr)
        elif tree.right:
            arr.append(None)
        if tree.right:
            self.toArray(tree.right,arr)
        
        return arr

print (Solution().isSameTree(p,q))