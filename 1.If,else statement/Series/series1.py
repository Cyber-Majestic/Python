#1+2+3+4+....+n
'''n=int(input("Enter the number of elements:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)   ''' 

n=int(input("Enter the number of elements:"))
sum=0
for i in  range(1,n+1,1):
    sum=sum+i
print(sum)    