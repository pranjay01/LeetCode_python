strs=["flower","flow","flight"]
result=''
tmpres=''

if len(strs)>1:
    i=0
    str1=strs[0]
    str2=strs[1]
    while i<len(str1) and i<len(str2):
        if str1[i]==str2[i]:
            result=result+str1[i]
            i=i+1
        else:
            break
    if len(result)>0:
        for index in range(2,len(strs)):
            str1=strs[index]
            i=0
            tmpres=''
            while i<len(str1) and i<len(result):
                if result[i]==str1[i]:
                    tmpres=tmpres+result[i]
                    i=i+1
                else:
                    result=tmpres
                    break
            if len(result)==0:
                return ('')
elif len(strs)==1:
    return (strs[0])
elif len(strs==0):
    return (result)
    
return (result)