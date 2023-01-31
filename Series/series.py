#1^2+2^2+3^2+....+n^2
n=int(input("Enter how many numbers:"))
sum=0
for i in range(1,n+1,1):
    sum=sum+pow(i,2)
print(sum)