heights = [2,1,5,6,2,3]
heights.append(0)
stackList1=[]
l=len(heights)
maxa=0
for i in range(l):
    if stackList1:
        tmp=stackList1[-1][1]
        if heights[i]>=tmp:
            stackList1.append((i,heights[i]))
        else:
            #k=1
            if tmp>maxa:
                maxa=stackList1[-1][1]
            t=stackList1[-1][0]
            tmp3=(i-t+1)*heights[i]
            if tmp3>maxa:
                maxa=tmp3
            stackList1.pop()
            while stackList1 and stackList1[-1][1]>heights[i]:
                tmp2=stackList1[-1]
                if tmp2[1]<tmp:
                    tmp=tmp2[1]
                tmp3=(i-tmp2[0])*tmp
                if tmp3>maxa:
                    maxa=tmp3
                t=stackList1[-1][0]
                stackList1.pop()
            # if stackList1:
            #     stackList1.append((i,heights[i]))
            # else:
            stackList1.append((t,heights[i]))

    else:
        stackList1.append((i,heights[i]))
print (maxa)
# if stackList2:
#     l=len(stackList2)
#     lastindex=stackList2[-1][0]
#     for i in range(l):
#         if i>0 and stackList2[i][1]==stackList2[i-1][1]:
#             continue
#         else:
#             tmp=(lastindex-stackList2[i][0]+1)*stackList2[i][1]
#             if tmp>maxa:
#                 maxa=tmp

