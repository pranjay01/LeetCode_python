height = [1,2,1]

ar=0
if height[0]<height[1]:
    ar=height[0]
else:
    ar=height[1]
big=0
small=0
if height[0]<height[1]:
    small=height[0]
    big=height[1]
else:
    small=height[1]
    big=height[0]



length = len(height)
for i in range(length):
    for j in range(i+1,length):
        if height[i]<=height[j] and (j-i)*height[i] > ar:
            ar=(j-i)*height[i]
        elif height[i]>=height[j] and (j-i)*height[j] > ar:
            ar=(j-i)*height[j]

print(ar)