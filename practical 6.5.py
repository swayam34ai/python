lst=[(123,23),(),("swayam",),()]
n=len(lst)
for i in range(n):
    if  lst[i]==():
        lst.remove(lst[i])
print(lst)
        
