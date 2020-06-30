haystack = ""
needle = ""

nl=len(needle)
hl=len(haystack)
i=0

#if nl == hl and haystack==needle:
#    print (0)

while i< hl-nl+1:
    if needle==haystack[i:i+nl]:
        print (i)
    i+=1
print (-1)