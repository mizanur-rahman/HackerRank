import math
def checkPrime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    if checkPrime(n):
        print('Prime')
    else:
        print('Not prime')
