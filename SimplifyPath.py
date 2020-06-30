path=".."

index=0
while index>=0:
    path = path.replace('//','/')
    index=path.find('//')

path = path.split('/')

index=0
l=len(path)
while index < l:
    if path[index]=='.':
        path.pop(index)
        l-=1
        continue
    elif path[index]=='..':
        path.pop(index)
        l-=1
        if index>0:
            path.pop(index-1)
            l-=1
            index-=1
    else:
        index+=1
if l==0:
    print ('/')
path='/'.join(path)
if l==1 or not path[0]=='/':
    path='/'+path
l=len(path)
if path[-1]=='/' and l>1:
    path=path[0:-1]



print (path)