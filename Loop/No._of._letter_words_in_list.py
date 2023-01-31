letters=0
numbers=0
words=0
text=input("Enter sentence:")
for i in text:
    i=i.lower()
    if i>='a' and i<='z':\
        letters=letters+1
    if i>='0' and i<='9':
        numbers=numbers+1
    if i==' ':
        words=words+1
print(letters)
print(numbers)
print(words+1)       
