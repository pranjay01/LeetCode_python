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

root=getTree([1,2,'null',3,'null',4,'null',5])

class Solution:
    def levelOrder(self, root: TreeNode) :
        res=[]
        level=[1]
        if root:
            self.toList(root,res,level)
        return res


    def toList(self,tree,tlist,level):
        #l=
        if len(tlist)<level[0]:
            tlist.append([])
            #l+=1
        if tree.left:
            level[0]+=1
            self.toList(tree.left,tlist,level)
        
        
        # if tree.right and not tree.left:
        #     tlist.append(None)

        tlist[level[0]-1].append(tree.val)

        if tree.right:
            level[0]+=1
            self.toList(tree.right,tlist,level)
        
        level[0]-=1
        return tlist
        #     index=0
        #     nodeQueue=[root]
        #     l=1
        #     lr=0
        #     tmp=[]
        #     count=1
        #     while index<l:
        #         if lr==count:
        #             res.append(tmp)
        #             tmp=[]
        #             count=count*2
        #             lr=0

        #         node = nodeQueue[index]

        #         if node:
        #             tmp.append(node.val)
        #             lr+=1
        #         else:
        #             #tmp.append(None)
        #             lr+=1
        #             index+=1
        #             continue
        #         if not node.left and not node.right:
        #             index+=1
        #             continue
        #         if node.left:
        #             nodeQueue.append(node.left)
        #             l+=1
        #         else:
        #             nodeQueue.append(None)
        #             l+=1

        #         if node.right:
        #             nodeQueue.append(node.right)
        #             l+=1
        #         else:
        #             nodeQueue.append(None)
        #             l+=1

        #         index+=1
        #     res.append(tmp)
        # return res

print (Solution().levelOrder(root))