import random
lst=[]
for i in range(20):
    lst.append(random.randrange(1,100,1))
print(lst)
a=int(input("enter number of your choice"))
position = []
for i in range(len(lst)):
    if lst[i]==a:
        position.append(i)
print(position if position else"not found")
       
