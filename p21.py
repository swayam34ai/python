a=input("enter your string")
l=0
b=0

for char in a:
    if char.isalpha():
        l+=1
    elif char.isdigit():
        b+=1
print(l,b)
