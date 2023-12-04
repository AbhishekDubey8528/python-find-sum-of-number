m=int(input("higher value"))
n=1
sum=0
while(n<=m):
    sum=sum+n
    n=n+1
    if(sum % 2 ==0):
        print(sum)
print(sum)