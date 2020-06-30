nums1 = [1, 3]
nums2 = [2]

len1=len(nums1)
len2=len(nums2)
totalL = len1 + len2
# even = True
# if totalL%2!=0:
#     even = False
tmp1=0
tmp2=0
medianL = int(totalL/2) +1
j=0
k=0
#newList=[]
if len1>0 and len2>0:
    for i in range(medianL):
        if nums1[j]<nums2[k]:
            if i==medianL-2:
                tmp1=nums1[j]
            elif i==medianL-1:
                tmp2=nums1[j]
            #newList.append(nums1[j])
            if j< len1-1:
                j += 1
            else:
                if j<medianL-2:
                    tmp1=nums2[medianL+k-j-1]
                    
                if j<medianL-1:
                    tmp2=nums1[medianL+k-j]
                #newList=#newList+nums2[k:medianL+k-j]
                break
        elif nums1[j]>nums2[k]:
            if i==medianL-2:
                tmp1=nums2[k]
            elif i==medianL-1:
                tmp2=nums2[k]
            #newList.append(nums2[k])
            if k< len2-1:
                k+=1
            else:
                if k<medianL-2:
                    tmp1=nums1[medianL-k+j-1]
                if k<medianL-1:
                    tmp2=nums1[medianL-k+j]
                #newList=#newList+nums1[j:medianL-k+j]
                break
        else:
            if i==medianL-2:
                tmp1=nums1[j]
                tmp2=nums2[k]
            elif i==medianL-1:
                tmp2=nums1[j]
            #newList.append(nums1[j])
            #newList.append(nums2[k])
            i+=1
            #end=False
            if j< len1-1:
                j += 1
            else:
                if j<medianL-2:
                    tmp1=nums1[medianL+k-j-1]
                if j<medianL-1:
                    tmp2=nums1[medianL-k+j]
                #newList=#newList+nums2[k:medianL+k-j]
                break
            if k<len2-1:
                k+=1
            else:
                if j<medianL-2:
                    tmp1=nums1[medianL-k+j-1]
                tmp2=nums1[medianL+k-j]
                #newList=#newList+nums1[j:medianL-k+j]
                break
                #end=True


# if len(#newList)<medianL:
#     if len1==0 :
#         #newList=#newList+nums2[k:medianL+k-j]
#     elif len2==0:
#         #newList=#newList+nums1[j:medianL-k+j]

if len1==0 :
    if medianL-2>=0:
        tmp1=nums2[medianL-2]
    tmp2=nums2[medianL-1]
elif len2==0:
    if medianL-2>=0:
        tmp1=nums1[medianL-2]
    tmp2=nums1[medianL-1]
# if totalL%2==0:
#     return (float(#newList[medianL-2]+#newList[medianL-1])/2)
# else:
#     return (float(#newList[medianL-1]))
if totalL%2==0:
    print (float(tmp1+tmp2)/2)
else:
    print (float(tmp2))
