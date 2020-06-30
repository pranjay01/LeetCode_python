class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-1*n
        elif n==0:
            return (1)
        if x==1:
            return (x)
        if x==-1:
            if n%2==0:
                return 1
            else:
                return -1

        if primeCheck(n):
            ori=x
            for i in range(n-1):
                    x=x*ori
                    if x<.00000001 and x>0:
                        return (0)
            return (x)

        ori=2
        while n>1:
            if n%ori==0:
                x=powf(x,ori)
                n=int(n/ori)
            else:
                ori+=1
        return (x)


def powf(x,y):
    ori=x
    for i in range(y-1):
        x=x*ori
    return (x)

def primeCheck(n):
    ori=int(math.sqrt(n))
    for i in range (2,ori):
        if n%i==0:
            return False
    return True