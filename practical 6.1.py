boys=("karan","arjun")
listn=[boys,"radha","tina"]
print(listn)
boys1=0
girls=0
for i in range(len(listn)):
    if type(listn[i])==str:
        girls+=1
    else:
        boys_count=len(listn[i])
        boys1+=boys_count
print(boys1,girls)
