n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

n = int(input("Enter number of rows: "))
for r in range(n):
    for c in range(n):
        if c==0 or r==(n-1) or r==c:
            print("*",end="")
        else:
            print(end=" ")
    print()