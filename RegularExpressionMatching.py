s='aa'
p='a.'

l=len(s)
i=0
pl=len(p)
p=list(p)
s=list(s)
if p[-1]=='.':
    p[-1]=s[-1]

if s==p:
    print (True)
    
while i<l:
    if i<pl:
        if p[i]==s[i]:
            i+=1
            continue
        elif p[i]=='.':
            if i>0:
                if p[i-1] is not '*':
                    p[i]=s[i]
                    i+=1
                    continue
                elif:
                    
                else:
                    tmp=i+1
                    while tmp<l:
                        if s[tmp].isalpha():
                            break
                        tmp+=1
                    tmp-=1
                    while tmp>=i:
                        p[tmp]=s[tmp]
                        tmp-=1
                    i-=1
                    continue

            else:
                p[i]=s[i]
                i+=1
        else:
            i+=1
    else:
        break

print (s==p)