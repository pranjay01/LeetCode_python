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

root=getTree([0,'null',-1])
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        num=[None,True]
        #ch=[True]
        if root:
            self.check(root,num)
        return num[1]
    
    
    def check(self,tree,num):
        if tree.left:
            self.check(tree.left,num)
        
        if num[0] is not None:
            if num[0]<tree.val:
                num[0]=tree.val
            else:
                num[1]=False
                return num
        else:
            #num.append(tree.val)
            num[0]=tree.val
        if tree.right:
            self.check(tree.right,num)
        
        return num

print(Solution().isValidBST(root))