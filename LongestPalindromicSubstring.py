s = "aaabaaaa"
maxl=0
length = len(s)
start=0
end=0
for i in range(length):
    
    j=length-1
 
    while j>i and j-i+1>maxl:
        tmp=i
        if s[j]==s[i]:
            tmp2=j
            psblen=j-i+1
            if psblen>maxl:
                pallindrome=True
                while tmp2>=tmp:
                    if s[tmp2]!=s[tmp]:
                        pallindrome=False
                        break
                    else:
                        tmp2=tmp2-1
                        tmp=tmp+1
                if pallindrome:
                    start=i
                    end=j
                    maxl=psblen

        j=j-1

print(s[start:end+1])