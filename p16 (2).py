def myfunction():
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t=input("enter your string")
    for i in t:
        if t in lower:
            t=t.upper()
            print(t)
myfunction()
