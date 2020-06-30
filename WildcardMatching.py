s="mississippi"
p="m*iss*iss*"

ind=0
while ind>=0:
    #p=p.replace('*?','*')
    #p=p.replace('?*','*')
    tmp=p.replace('*','')
    p=p.replace('**','*')
    ind = p.find('**')
start=0
tmp=''
lp=len(p)
ls=len(s)
if len(tmp)>ls:
    print (False)
i=0
tmp=''
while i <lp and start < ls:
    if p[i] == '*':
        if i < (lp-1):
            #t=p[i+1]
            j=i+1
            pa=''
            while j<lp:
                if p[j].isalpha():
                    pa=pa+p[j]
                    j+=1
                else:
                    break
            if not pa:
                if j==lp-1:
                    if start<ls-1:
                        ind=ls
                        i=j
                    else:
                        print (False)
                else:
                    ind=start
            else:
                ind=s.rfind(pa,start,ls)
            if ind<0:
                print (False)
                break
            else:
                tmp=tmp+s[start:ind]
                start=ind
                #i+=1
        else:
            if lp==1:
                print (True)
                break
            else:
                #ind=s.find(tmp,0,ls)
                tmp=tmp+s[len(tmp):]
    elif p[i]=='?':
        tmp=tmp+s[start:start+1]
        start+=1
    else:
        if p[i]==s[start]:
            tmp=tmp+s[start:start+1]
            start+=1
        else:
            print (False)
            break
    i+=1

if i<lp:
    tmp=tmp+p[i:lp]
    ind=0
    while ind>=0:
        tmp=tmp.replace('*','')
        ind = tmp.find('*')
if tmp==s:
    print (True)
else:
    print (False)
