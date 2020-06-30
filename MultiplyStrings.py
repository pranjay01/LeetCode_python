num1="408"
num2="50"
import math

dict_stn={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
dict_nts={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

n1=0
n2=0
for char in num1:
    n1=n1*10 + dict_stn[char]

for char in num2:
    n2=n2*10 + dict_stn[char]

num1=n1*n2
num1=num1
num2=''
n1 = int(math.log10(num1))+1
while n1>0:
    n2=pow(10,(n1-1))
    num2=num2+dict_nts[int(num1/n2)]
    num1=num1%n2
    n1-=1



print(num2)
