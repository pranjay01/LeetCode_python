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

root=getTree([3,4,4,5,'null','null',5,6,'null','null',6])

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        res=[]
        level=[1]
        l=[0]
        if root:
            self.toList(root,res,level,l)
            for List in res:
                if self.checkmirror(List):
                    continue
                else:
                    return False
            
        return True

    def checkmirror(self,res):
        l=len(res)
        i=0
        j=l-1
        while i<j:
            if not res[i]==res[j]:
                return False
            i+=1
            j-=1
        return True
    def toList(self,tree,tlist,level,l):
        #l=[len(tlist)]
        if l[0]<level[0]:
            tlist.append([])
            l[0]+=1
        if tree.left:
            level[0]+=1
            self.toList(tree.left,tlist,level,l)
        
        
        if tree.right and not tree.left:
            t=level[0]
            if t+1>l[0]:
                tlist.append([None])
                l[0]+=1
            else:
                tlist[t].append(None)

        tlist[level[0]-1].append(tree.val)

        if tree.right:
            level[0]+=1
            self.toList(tree.right,tlist,level,l)

        if not tree.right and tree.left:
            t=level[0]
            if t+1>l[0]:
                tlist.append([None])
                l[0]+=1
            else:
                tlist[t].append(None)

        if not tree.right and not tree.left:
            t=level[0]
            if t+1>l[0]:
                tlist.append([None,None])
                l[0]+=1
            else:
                tlist[t].append(None)
                tlist[t].append(None)

        level[0]-=1
        return tlist


print (Solution().isSymmetric(root))