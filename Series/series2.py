#2+4+6+8+...+n
n=int(input("Enter the number of elements:"))
sum=0
for i in range(2,2*n,2):
     sum=sum+i
print(sum)