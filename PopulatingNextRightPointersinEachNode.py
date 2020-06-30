#Nice Logic
#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/705526/go-iterative-100-runtime-(0ms)-and-97.09-memory-(6MB)
class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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
    return root

root=getTree([1,2,3,4,5,6,7])
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            level=[1,0]
            tList=[]
            self.toList(root,level,tList)
            # for List in tList:
            #     l=len(List)-1
            #     for i in range(l):
            #         List[i].next=List[i+1]
            #     List[-1].next=None
            #print (tList)
        return root
    def toList(self,root,level,tList):
        if level[1]<level[0]:
            tList.append([])
            level[1]+=1

        if root.left:
            level[0]+=1
            self.toList(root.left,level,tList)
        tmp=level[0]-1
        if tList[tmp]:
            tList[tmp][-1].next=root
        tList[level[0]-1].append(root)

        if root.right:
            level[0]+=1
            self.toList(root.right,level,tList)

        level[0]-=1

print(Solution().connect(root))