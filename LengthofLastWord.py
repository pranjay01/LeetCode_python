s="Hello    World    "
if not s:
    print (0)
else:
    tmp=s.split(" ")
    maxl=0
    while maxl==0 and tmp:
        maxl=len(tmp[-1])
        tmp.pop()

print (maxl)