class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1=len(nums1)
        len2=len(nums2)
        totalL = len1 + len2
        # even = True
        # if totalL%2!=0:
        #     even = False

        medianL = int(totalL/2) +1
        j=0
        k=0
        newList=[]
        if len1>0 and len2>0:
            for i in range(medianL):
                if nums1[j]<nums2[k]:
                    newList.append(nums1[j])
                    if j< len1-1:
                        j += 1
                    else:
                        newList=newList+nums2[k:medianL+k-j]
                        break
                elif nums1[j]>nums2[k]:
                    newList.append(nums2[k])
                    if k< len2-1:
                        k+=1
                    else:
                        newList=newList+nums1[j:medianL-k+j]
                        break
                else:
                    newList.append(nums1[j])
                    newList.append(nums2[k])
                    i+=1
                    #end=False
                    if j< len1-1:
                        j += 1
                    else:
                        newList=newList+nums2[k:medianL+k-j]
                        break
                    if k<len2-1:
                        k+=1
                    else:
                        newList=newList+nums1[j:medianL-k+j]
                        break
                        #end=True


        if len(newList)<medianL:
            if len1==0 :
                newList=newList+nums2[k:medianL+k-j]
            elif len2==0:
                newList=newList+nums1[j:medianL-k+j]

        if totalL%2==0:
            return (float(newList[medianL-2]+newList[medianL-1])/2)
        else:
            return (float(newList[medianL-1]))










############################################################################

