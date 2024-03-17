n=int(input("enter the number:\n"))
a=(n//2+1)*n
for i in range(1,n+1):
    for j in range(1,1+i):
        print(a,end=" ")
        a=a-1
    print()
