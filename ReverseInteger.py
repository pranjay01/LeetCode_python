x = 120

ispositive=True
if x<0:
    x=x*(-1)
    ispositive=False

result = 0.0
i=len(str(x))-1
while x>0:
    result = result + int(x%10)*pow(10,i)
    i=i-1
    x = int(x/10)

if ispositive:
    if result <= 2147483647:
        print(int(result)) 
    else:
        print( 0)
else:
    if result <= 2147483648:
        print( int(result*(-1)))
    else:
        print( 0)



