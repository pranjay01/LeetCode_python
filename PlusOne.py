digits=[8,9,9]

l = len(digits)
for i in reversed(range(0,l)):
    if digits[i]==9:
        digits[i]=(digits[i]+1)%10
    else:
        digits[i]+=1
        break
else:
    digits.insert(0,1)



print (digits)