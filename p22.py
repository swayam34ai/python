































































vowels = "a,e,i,o,u,A,E,I,O,U"
str = input("enter your string")
count=0
for i in str:
    if i in vowels:
        count=count+1    
print(count)
