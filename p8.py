def year():
    a=int(input("enter a year"))
    if a%4==0:
          print("it is a leap year")
    elif a%100==0:
        print("it is a leap year")
    elif a%400==0:
        print("it is a leap year")
    else:
        print("not a leap year")
year()
year()
