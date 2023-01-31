n=input("Enter a text of numbers:")
list=n.split()
print(list)
sum=0
for i in list:
    sum=sum + int(i)
print(sum)