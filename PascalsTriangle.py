numRows=5
class Solution:
    def generate(self, numRows: int):
        # if numRows==1:
        #     return[[1]]
        # if numRows==2:
        #     return[[1],[1,1]]
        res=[]
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])  
        return res
print (Solution().generate(numRows))