import random
lst=[]
for i in range(30):
    lst.append(random.randrange(-100,100,1))
print(lst)
positive=[]
negative=[]
for j in lst:
    if j>=0:
        positive.append(j)
    else:
        negative.append(j)
print("positve,negative",positive,negative)

