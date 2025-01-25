def s():

    x=int(input("enter the x coordinate of centre of circle"))
    y=int(input("enter the y coordinate of centre of circle"))
    r=int(input("enter the radius of circle"))
    p1=int(input("enter the x coordinate of point you want to consider"))
    p2=int(input("enter the y coordinate of point you want to consider"))
    d=((p1-x)^2+(p2-y)^2)
    if d>r:
        print("the point is outside the circle")
    elif d<r:
        print("the point is inside the circle")
    elif d==r:
        print("the point lies on the circle")
s()
s()