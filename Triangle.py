triangle=[[2],[3,4],[6,5,9],[4,4,8,0]]

class Solution:
    def minimumTotal(self, triangle) -> int:
        l=len(triangle)
        if l>0:
                =[]
            prev=triangle[0]
            for i in range(1,l):
                tmp=triangle[i]
                for j in range(i+1):
                    if j==0:
                        List.append(prev[j]+tmp[j])
                    elif(j==i):
                        List.append(prev[j-1]+tmp[j])
                    else:
                        List.append(min((prev[j]+tmp[j]),(prev[j-1]+tmp[j])))
                prev=List[:]
                List.clear()
        else:
            List=[0]
        return  min(prev)

print (Solution().minimumTotal(triangle))