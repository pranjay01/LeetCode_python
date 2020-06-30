a = "0"
b = ""

la=len(a)
lb=len(b)
limit =la
if la>=lb:
    s='0'*(la-lb)
    b=s+b
    limit=la
else:
    s='0'*(lb-la)
    a=s+a
    limit=lb
carry=0
res=''
for i in reversed(range(0,limit)):
    tmp = carry + int(a[i]) + int(b[i])
    if tmp==0:
        res='0'+res
    elif tmp ==1:
        res='1'+res
        carry=0
    elif tmp==2:
        res='0'+res
        carry=1
    else:
        res='1'+res
        carry=1


    

if carry==1:
    res='1'+res

print (res)
