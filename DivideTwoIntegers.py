dividend = -2147483648
divisor = -1
#-2147483648
#-2147483648
#-1

def getresult(divisor,dividend):
    if divisor>dividend:
        return (0)  
    initDiv=divisor
    #initDividend=dividend
    result=1
    tmp=divisor
    divisor+=divisor
    while divisor<=dividend:
        tmp=divisor
        result+=result
        divisor+=divisor
    divisor=tmp
    if dividend>divisor:
        result=result+getresult(initDiv,dividend-divisor)
        return result
    else:
        return result


isp=True
if divisor<0:
    isp=False
    divisor=divisor*-1
if dividend<0:
    if isp:
        isp=False
    else:
        isp=True
    dividend=dividend*-1

#result = 0

#if divisor>dividend:
#    print (result)
#else:
result = getresult(divisor,dividend)

if not isp:
    result=result*-1

if result<-2147483648 or result>2147483647:
    print (2147483647)
else:
    print (result)