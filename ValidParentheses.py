s="]"

store=[]

for b in s:
    if b==')':
        if store and store[-1]=='(':
            store.pop(-1)
        else:
            print (False)
    elif store and b=='}':
        if store[-1]=='{':
            store.pop(-1)
        else:
            print (False)
    elif store and b==']':
        if store[-1]=='[':
            store.pop(-1)
        else:
            print (False)
    else:
        store.append(b)

if len(store)>0:
    print (False)
else:
    print (True) 