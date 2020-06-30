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

root=getTree([3,9,20,'null','null',15,7])

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        l=[0,1]
        if root:
            self.toList(root,l)
        return l[0]


    def toList(self,tree,l):
        if l[0]<l[1]:
            l[0]+=1
        if tree.left:
            l[1]+=1
            self.toList(tree.left,l)
                
        if tree.right and not tree.left:
            #t=l[1]
            if l[1]+1>l[0]:
                l[0]+=1
        if tree.right:
            l[1]+=1
            self.toList(tree.right,l)

        if not tree.right and tree.left:
            #t=l[1]
            if l[1]+1>l[0]:
                l[0]+=1
        l[1]-=1
        return l
        

print (Solution().maxDepth(root))