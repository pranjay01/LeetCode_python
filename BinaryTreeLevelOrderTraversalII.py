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
    def levelOrderBottom(self, root: TreeNode) :
        res=[]
        level=[1]
        if root:
            self.toList(root,res,level)
            level=len(res)
            res.reverse()
        return res


    def toList(self,tree,tlist,level):
        if len(tlist)<level[0]:
            tlist.append([])
        if tree.left:
            level[0]+=1
            self.toList(tree.left,tlist,level)

        tlist[level[0]-1].append(tree.val)

        if tree.right:
            level[0]+=1
            self.toList(tree.right,tlist,level)
        
        level[0]-=1
        return tlist
        

print (Solution().levelOrderBottom(root))