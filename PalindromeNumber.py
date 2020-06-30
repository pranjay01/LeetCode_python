x = 13531

if x<0:
    print (False)

elif x==0:
    print (True)

else:
    # nn = 0
    # act=x
    # p = pow(10,(len(str(x))-1))
    # while x>0:
    #     nn = nn + int(x%10)*p
    #     p=int(p/10)
    #     x = int(x/10)
    # if nn==act:
    #     return (True)
    # else:
    #     return (False)
    if x%11 == 0:
        print( True)
    else:
        p1 = pow(10,(len(str(x))-1))
        p2 =10
        while x>0:
            if (int(x/p1)==x%p2):
                x=x%p1
                x=int(x/p2)
                p1=int(p1/100)
                #p2=p2*10
            else:
                print(False)
        print(True)
