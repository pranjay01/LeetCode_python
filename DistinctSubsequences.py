#S="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
#T="bcddceeeebecbc"
S = "babgbag"
T = "bag"
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        row1=[]
        row2=[]
        m=len(t)+1
        n=len(s)+1
        for i in range(m):
            for j in range(n):
                if i==0:
                    row1.append(1)
                    continue
                if j==0:
                    row1.append(0)
                    continue

                if t[i-1]==s[j-1]:
                    row1.append(row1[j-1]+row2[j-1])
                else:
                    row1.append(row1[j-1])
            row2=row1[:]
            row1.clear()
        return(row2[-1])

print(Solution().numDistinct(S,T))