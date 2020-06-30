nums =[0,0,1,2,0,2,1,1,0,1,1,0,1,0,2,2,0,0,2,2,2,1,0,2,1,1,1,2,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,2,0,1,1,2,1,1,2,2,0,1,1,1,0,0,2,1,2,0,2,0,1,2,2,2,0,2,0,2,1,2,1,2,0,0,1,1,2,0,1,2,0,0,1]

pointer0=-1
pointer1=-1
pointer2=-1

l=len(nums)
index=0
while index<l:
    if nums[index]==0:
        if pointer0<0:
            pointer0=index
            if pointer2>=0 or pointer1>=0:
                nums.pop(index)
                nums.insert(0,0)
                pointer0=0
                if pointer2>=0:
                    pointer2+=1
                if pointer1>=0:
                    pointer1+=1
            
        else:
            if pointer1<0 and pointer2<0:
                pointer0+=1
                pass
            else:
                nums.pop(index)
                nums.insert(0,0)
                pointer0+=1
                if pointer2>=0:
                    pointer2+=1
                if pointer1>=0:
                    pointer1+=1

    elif nums[index]==1:
        if pointer1<0:
            pointer1=index
            if pointer2>=0:
                nums.pop(index)
                pointer2+=1
                nums.insert(pointer0+1,1)
                pointer1=pointer0+1
        else:
            if pointer2>=0:
                nums.pop(index)
                pointer2+=1
                nums.insert(pointer0+1,1)
                pointer1+=1
            
    else:
        if pointer2<0:
            pointer2=index
        else:
            pointer2+=1
    index+=1

print (nums)