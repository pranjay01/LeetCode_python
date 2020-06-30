nums1 = [1,2,3,7,0,0,0]
m = 4
nums2 = [2,5,6]
n = 3

l=len(nums1)
i=0
j=0

while i<l and j<n:
    if nums1[i]<nums2[j]:
        i+=1
        continue
    else:
        nums1.pop()
        nums1.insert(i,nums2[j])
        m+=1
        i+=1
        j+=1

i=m
while j<n:
    nums1.pop()
    nums1.insert(i,nums2[j])
    i+=1
    j+=1

print (nums1)