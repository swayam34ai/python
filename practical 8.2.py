import random
d1=[]
for i in range(10):

    d1.append(random.randrange(15,45,1))

print(d1)
d1=set(d1)
count=0
d2=set([])
for i in d1:
    if  i<=30:
        count+=1
    elif i>35:
        d2.add(i)
d1=d1-d2
print(count,d2,d1)
