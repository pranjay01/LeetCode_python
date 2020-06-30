n=0

# mirror approach

if n==0:
    print([0])

res=[0,1]

for i in range(2,n+1):
    cnstadd=pow(2,i-1)
    l=len(res)
    for i in reversed(range(l)):
        res.append(cnstadd+res[i])

print (res)