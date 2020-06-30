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

root=getTree([1,2,3])
#q=getTree([1,"null",2])
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr1=[]
        self.toList(root,arr1)
        print (arr1)   
        num1=None
        num2=arr1[-1]
        l=len(arr1)
        i=0
        arr2=[]+arr1
        arr2.sort()
        for i in range(l):
            if not arr1[i]==arr2[i]:
                if num1:
                    num2=arr1[i]
                    break
                num1=arr1[i]
        self.replace(root,num1,num2)

        print(root)

    def replace(self,tree,num1,num2):
        if tree.left:
            self.replace(tree.left,num1,num2)

        if tree.val==num1:
            tree.val=num2
        elif tree.val==num2:
            tree.val=num1

        if tree.right:
            self.replace(tree.right,num1,num2)

        return 0        

    def toList(self,tree,tlist):
        if tree.left:
            self.toList(tree.left,tlist)
        
        tlist.append(tree.val)

        if tree.right:
            self.toList(tree.right,tlist)
        
        return tlist


Solution().recoverTree(root)