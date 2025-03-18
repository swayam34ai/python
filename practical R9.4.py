def  reverse(lst,n):
    
    if n==0:
        return lst
    if n!=0:
        l=n%10
        
        lst+=[l]
        print(lst)
        if n//10==0:
            print("this is ex")
            return lst
        
        reverse(lst,n//10)
    else:
        return lst
a=int(input("enter number"))
l=reverse([],a)
print(l)
