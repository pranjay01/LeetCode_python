s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not len(s1)+len(s2) == len(s3):
            return False
        return self.check(s1,s2,s3)

    def check(self,s1,s2,s3):
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3


print (Solution().isInterleave(s1,s2,s3))