s=''
length=len(s)
result=0
mapr={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for index in range(length):
    if index==0:
        result = mapr[s[index]]
    else:
        if mapr[s[index-1]]<mapr[s[index]]:
            result = result + mapr[s[index]] - 2*mapr[s[index-1]]
        else:
            result =result + mapr[s[index]]
print(result)