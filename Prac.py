n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print("\n")
    
for i in range(n-1,0,-1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for j in range(2*i-1,0,-1):
        print("*",end="")
    print("\n")