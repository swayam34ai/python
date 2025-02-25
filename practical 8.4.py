set1=("abc","bfhfd","geg")
set2=set()
set3=set()
for i in set1:
    if i[0]=='a' or i[0]=='A':
        set2.add(i)
    elif i[0] =='b' or i[0]=="B":
        set3.add(i)
print(set2,set3)
    
