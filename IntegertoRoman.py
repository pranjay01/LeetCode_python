num =3999

dict = {1:'I',4:'IV', 5:'V',9:'IX', 10:'X',40:'XL',50:'L',90:'XC',
        100:'C',400:'CD',500:'D',900:'CM',1000:'M'}

length = len(str(num))
res0=""
res1=""
res2=""
res3=""
for i in range(length):
    tmp = num%10
    while tmp>0 and i==0:
        if tmp < 5:
            if tmp == 4:
                res0 = res0 + dict[4]
                tmp = tmp-4
            else:   
                res0=res0+dict[1]
                tmp=tmp-1
        elif tmp >= 5:
            if tmp==9:
                res0 = res0+dict[9]
                tmp=tmp-9
            else:
                res0 = res0 + dict[5]
                tmp = tmp-5
                
    while tmp>0 and i==1:
        if tmp < 5:
            if tmp == 4:
                res1 = res1 + dict[40]
                tmp = tmp-4
            else:   
                res1=res1+dict[10]
                tmp=tmp-1
        elif tmp >= 5:
            if tmp==9:
                res1 = res1+dict[90]
                tmp=tmp-9
            else:
                res1 = res1 + dict[50]
                tmp = tmp-5
    while tmp>0 and i==2:
        if tmp < 5:
            if tmp == 4:
                res2 = res2 + dict[400]
                tmp = tmp-4
            else:   
                res2=res2+dict[100]
                tmp=tmp-1
        elif tmp >= 5:
            if tmp==9:
                res2 = res2+dict[900]
                tmp=tmp-9
            else:
                res2 = res2 + dict[500]
                tmp = tmp-5
    while tmp>0 and i==3:
        res3=res3+dict[1000]
        tmp=tmp-1
  
    num=int(num/10)
    if num==0:
        break
print(res3+res2+res1+res0)
             