prices=[3,3,5,0,0,3,1,4]

class Solution:
    def maxProfit(self, prices) -> int:
        l=len(prices)
        min1=max(prices)
        prf1=0
        i=0
        list1=[]
        for i in range(l):
            tmp=prices[i]
            min1=min(tmp,min1)

            prf1=max(prf1,(tmp-min1))
            list1.append(prf1)
        min1=prices[-1]
        prf1=0
        for i in reversed(range(l)):
            tmp=prices[i]
            min1=max(min1,tmp)

            prf1=max(prf1,(min1-tmp))
            #list2.append(prf1)
            list1[i]+=prf1
        return max(list1)
print(Solution().maxProfit(prices))