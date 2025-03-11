def count_lower_upper(x):
    lowercount=0
    uppercount=0
    for i in x:
        if i.islower():
            lowercount+=1
        elif i.isupper():
            uppercount+=1
    return{lowercount,uppercount}
    
print(count_lower_upper("swaYAMW"))
            
