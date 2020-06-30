m=10
n=10

#m=3
#//n=7

m-=1
n-=1
tm=max(m,n)
tn=min(m,n)

def fact(m,n):
    if m<=n:
        return 1
    else:
        return(m*fact(m-1,n))

#res=fact(m+n-2)/(fact(m-1)*fact(n-1))
res = fact(tm+tn,tm)/fact(tn,1)
print (int(res))