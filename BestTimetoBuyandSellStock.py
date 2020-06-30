prices=[1,2]


class Solution:
    def maxProfit(self, prices) -> int:
        minv=max(prices)
        profit=0
        l=len(prices)
        for i in range(l):
            tmp=prices[i]
            if tmp<minv:
                minv=tmp

            if tmp-minv>profit:
                profit=tmp-minv
        return profit

print(Solution().maxProfit(prices))