
def decimal_to_binary(n,d=2):
    
        
    r=n%d
    if n:
        decimal_to_binary(n//d)
        if r!=None:
            print(r,end='')
    
        

print(decimal_to_binary(45))
