words = ["What","must","be","acknowledgment","shall","be"]
#words = ["Science","is","what","we","understand","well","enough","to","explain",
#         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16

def getStr(words,l,maxWidth,count):
    #count=
    i=0
    while l<maxWidth:
        words[i]=words[i]+' '
        l+=1
        i+=1
        if i>=count:
            i=0
    return (''.join(words))



i=0
st=0
res=[]
l=0
wrdLen=len(words)
tmp=[]
while i<wrdLen:
    tmpwrd=words[i]
    l=l+len(tmpwrd)
    tmp.append(tmpwrd)
    if l==maxWidth:
        tmp=' '.join(tmp)
        res.append(tmp)
        tmp=[]
        st=i+1
        l=0
        i+=1
        continue
    elif l>maxWidth:
        #i-=1
        l=l-(i-st)-len(tmpwrd)
        tmp.pop()
        res.append(getStr(tmp,l,maxWidth,i-st-1))
        tmp=[]
        st=i
        l=0
        #i-=1
        continue
    l+=1
    i+=1

l-=1
if l>0:
    tmp=' '.join(words[st:])
    tmp=tmp+ (' '*(maxWidth-l))
    res.append(tmp)
print (res)


print (len(res[-1]))
