rowIndex=30
class Solution:
    def generate(self, rowIndex: int):
        rowIndex+=1
        currR=[]
        prevR=[]
        for i in range(rowIndex):
            for j in range(i+1):
                if j==0 or j==i:
                    currR.append(1)
                else:
                    currR.append(prevR[j-1] + prevR[j])  
            prevR=currR[:]
            currR.clear()
        return prevR
print (Solution().generate(rowIndex))