n=int(input("enter the number:\n"))
for i in range(n):
    for j in range(i,i+n):
        print(chr(j + 65), end=" ")
    print()
