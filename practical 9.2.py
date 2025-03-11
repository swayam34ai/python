def compute(n):
    nn = int(str(n) * 2)  
    nnn = int(str(n) * 3)  
    nnnn = int(str(n) * 4)
    result=n+nn+nnn+nnnn
    return result
for i in range(4,8):
    print(compute(i))
    
