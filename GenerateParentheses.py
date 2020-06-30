n=0

resultset=set()

resultset.add("()")
for count in range(n-1):
    tmp = set()
    for string in resultset:
        length = len(string)
        for index in range(length):
            tmp.add(string[:index]+"()"+string[index:])
    resultset=tmp

resultset = list(resultset)
print(resultset)