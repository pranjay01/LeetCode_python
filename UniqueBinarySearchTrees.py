n=3

class Solution:
    def numTrees(self, n: int) -> int:
        #a=self.fact(2*n)
        #b=self.fact(n)
        #c=b*(n+1)
        return int((self.fact(2*n))/((n+1)*pow((self.fact(n)),2)))


    def fact(self,n):
        if n==1 or n==0:
            return 1
        return n*self.fact(n-1)
print (Solution().numTrees(n))

print (Solution().fact(n))