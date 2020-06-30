s="tmmzuxt"
length = len(s)
maxl=0
tmp=0
dicts = {}
start = 0
d = True
for i in range(length):
    d=True
    if s[i] in dicts and dicts[s[i]]>=0:
        d=False
        tmp=i - start
        start = dicts[s[i]]+1
        dicts[s[i]]=i
        if tmp > maxl:
            maxl=tmp
        for key in dicts:
            if(dicts[key]<start):
                dicts[key] = -1
    else:
        dicts[s[i]]=i
        
    if i==length-1 and d:
        if length-start > maxl:
            maxl=length-start

print(maxl)