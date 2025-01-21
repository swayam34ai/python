x1=int(input("enter first number"))
y1=int(input("enter second number"))
x2=int(input("enter third number"))
y2=int(input("enter fourth number"))
x3=int(input("enter fifth number"))
y3=int(input("enter sixth number"))
m=y2-y1/x2-x1
n=y3-y1/x3-x1
if m==n:
    print("the points are in a line")
else:
    print("the points are not in a line")
    
