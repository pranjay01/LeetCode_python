n=3

def getFact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*getFact(n-1)

twoCount = int(n/2)
if n%2==0:
    oneCount=0
else:
    oneCount=1
total = 1
mFact = getFact(twoCount+oneCount)
m1Fact=1
if oneCount==0:
    m2Fact=mFact
else:
    m2Fact=mFact/(twoCount+oneCount)
while oneCount<n:
    total=total + (mFact)/(m1Fact*m2Fact)
    twoCount-=1
    oneCount+=2
    mFact=mFact*(twoCount+oneCount)
    m1Fact=m1Fact*(oneCount-1)*oneCount
    m2Fact=m2Fact/(twoCount+1)

print (total)