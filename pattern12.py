n=int(input("enter the number:\n"))
for i in range(1, n*2,2 ):
    for j in range(i, i+n*2,2 ):
        print(j, end=' ')
    print()
