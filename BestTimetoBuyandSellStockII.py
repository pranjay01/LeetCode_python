prices=[2,1,2,0,1]


class Solution:
    def maxProfit(self, prices) -> int:
        profit=0
        minval=-1
        l=len(prices)-1
        i=0
        while i<l:
            tmp=prices[i]
            if minval==-1:
                if prices[i+1]>tmp:
                    minval=tmp
                i+=1
            else:
                if prices[i+1]<=tmp:
                    profit=profit+(tmp-minval)
                    minval=-1
                i+=1
        if minval>=0:
            profit=profit+(prices[i]-minval)
        return profit
                    
                


print(Solution().maxProfit(prices))