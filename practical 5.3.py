import random
lst=[]
for i in range(50):
    lst.append(random.randrange(1,30,1))
print(lst)
x=[]
for j in lst:
    if j not in x:
        x.append(j)
print(x)


