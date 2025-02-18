import datetime
def tuple3():
    d1=(1,1,2014)
    d2=(5,1,2014)
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d2[2],d2[1],d2[0])
    print(date1,date2)
    x=abs(date2-date1)
    print(x)
tuple3()
