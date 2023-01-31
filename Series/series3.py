#1+3+5+7+...+2*n+1
n=int(input("Enter how many numbers:"))
sum=0
for i in range(1,2*n+1,2):
    sum=sum+i
print(sum)