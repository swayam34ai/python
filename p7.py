def ls3():
    a=int(input("enter you number"))
    b=int(input("enter you second number"))
    c=int(input("enter you third number"))
    largest = a
    if largest<b:
        largest=b
    if largest<c:
        largest=c

    sml = a
    if b<sml:
        b=sml
    if c<sml:
        c=sml


    if sml==largest:

        print("they are same")
    else:
        print(largest,"largest",sml,"smallest")

ls3()
ls3()


