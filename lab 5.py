import random
odd=[]
even=[]
new=[]
for i in range(5):
    odd.append(random.randrange(1,100,2))
print(odd,end='')
for j in range(4):
    even.append(random.randrange(0,100,2))
print(even)
odd.pop(2)
odd.insert(2,even)
for x in odd:
    if isinstance(x,list):
        new.extend(x)
    else:
        new.append(x)

print(odd)
print(new)
