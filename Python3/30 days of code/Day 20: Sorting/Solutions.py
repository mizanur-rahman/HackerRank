import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalSwap=0
sortedList=[]
for i in range(n-1):
    numSwap=0
    for j in range(n-1):
        if  a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            numSwap+=1
    totalSwap+=numSwap

    if numSwap==0:
        break

    
print(f'Array is sorted in {totalSwap} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[n-1]}')
