n=int(input("enter the number:\n"))

for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=' ')
    print()
