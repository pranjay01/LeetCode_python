nums=[1,2,0,1]

class Solution:
    def longestConsecutive(self, nums) -> int:
        maxc=0
        count=1
        nums.sort()
        l=len(nums)
        if l==0:
            return maxc
        i=1
        prev=nums[0]
        while i<l:
            curr=nums[i]
            if curr==prev:
                i+=1
                continue
            if curr==prev+1:
                count+=1
            else:
                maxc=max(maxc,count)
                count=1
            i+=1
            prev=curr
        maxc=max(maxc,count)
        return maxc

print (Solution().longestConsecutive(nums))