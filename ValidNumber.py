#s=".e1"
#s=".2e81"
s=" -.7e+0435"
s=s.strip()
l=len(s)
if not l:
    print (False)
counte=0
countd=0
counts=0
for i in range(l):
    if s[i].isdigit():
        continue
    elif s[i] == 'e':
        if not (i==0 or i==l-1) and counte<1 and not(s[i-1]=='-' or s[i-1] =='+') :
            counte+=1
            counts-=1
        else:
            print (False)
        
        
    elif (s[i].isalpha()):
        print (False)
    elif s[i]=='.':
        if countd<1 and counte<1 and l>1 :
            countd+=1
        else:
            print (False)
        if i==l-1:
            if not (s[i-1].isdigit()):
                print (False)
        elif i==0:
            if not (s[i+1].isdigit()):
                print (False)
        else:
            if not (s[i-1].isdigit() or s[i+1].isdigit()):
                print (False)

    elif s[i]=='-' or s[i]=='+':
        if counts<1 and l>1:
            counts+=1
        else:
            print (False)
        if not (i==0 or (s[i-1]=='e' and i<l-1)):
            print (False)
    elif s[i]==" ":
        print (False)
print (True)

print (s)