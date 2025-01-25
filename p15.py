def marks():
    x=int(input("enter the marks of maths"))
    y=int(input("enter the marks of physics"))
    z=int(input("enter the marks of chemistry"))
    print(x+y+z="total")
    print(x+y+z/3="average")
    if x<=39 or y<=39 or z<=39:
        print("you are fail")
    if x>0 and x<=39 or y>0 and y<=39 or z>0 and z<=39:
        print("grade f")
    elif x>39 and x<=44 or y>39 and y<=44 or z>39 and z<=44:
        print("grade p")
     elif x>44 and x<=49 or y>44 and y<=49 or z>44 and z<=49:
        print("grade c")
     elif x>49 and x<=54 or y>49 and y<=54 or z>49 and z<=54:
        print("grade b")
     elif x>54 and x<=59 or y>54 and y<=59 or z>54 and z<=59:
        print("grade b+")
     elif x>59 and x<=69 or y>59 and y<=69 or z>59 and z<=69:
        print("grade a")
    elif x>69 and x<=79 or y>69 and y<=79 or z>69 and z<=79:
        print("grade a+")
    elif x>79 and x<=100 or y>79 and y<=100 or z>79 and z<=100:
        print("grade o")
marks()
marks()

    
