n=int(input("enter the number:\n"))
p = 2
for i in range(1, n+1):
    for j in range(1, i + 1):
       print(p, end=" ")
       p += 2
    print()
