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
root=getTree([5,4,8,11,'null',13,4,7,2,'null','null',5,1])

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res=[]
        tmp=[]
        if root:
            self.check(root,sum,res,tmp)
            
        return res
        
    def check(self,root,sum,res,tmp):
        if root:
            tmp.append(root.val)
            sum=sum-root.val
        if sum==0 and not root.left and not root.right:
            res.append(tmp[:])
        if root.left:
            self.check(root.left,sum,res,tmp)

        if root.right:
            self.check(root.right,sum,res,tmp)

        tmp.pop()

print(Solution().hasPathSum(root,22))