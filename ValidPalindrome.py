s="  "


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=len(s)
        i=0
        j=l-1

        while i<j:
            si=s[i]
            sj=s[j]
            if si.isalnum() and sj.isalnum():
                if si==sj:
                    i+=1
                    j-=1
                    continue
                else:
                    return False
            if not si.isalnum():
                i+=1
            if not sj.isalnum():
                j-=1
        return True

print(Solution().isPalindrome(s))