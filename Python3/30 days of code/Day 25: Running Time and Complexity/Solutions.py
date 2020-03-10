T=int(input())
for i in range(0,T):
    n=int(input())
    p=0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            p=1
            break
    if n==1 or p==1:
        print('Not prime')
    else:
        print('Prime')
