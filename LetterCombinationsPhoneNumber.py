digits="23"
mobdict={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],
     "6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}


if len(digits)==0:
    print ([])
elif len(digits)==1:
    print (mobdict[digits])
else:
    result=['']    
    for char in digits:
        tmp=[]
        for index in result:
            for letter in mobdict[char]:
                tmp.append(index+letter)
        result=tmp   

print(result)