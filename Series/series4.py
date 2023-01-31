#1+1/2+1/3+....+1/N
n=int(input("Enter how many numbers:"))
sum=0
for i in range(1,n+1,1):
    sum=sum+1/i
print(sum)
