class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

    def __str__(self):
        return f"{self.date[0]:02}/{self.date[1]:02}/{self.date[2]}"

print("Enter first date:")
d1 = int(input("Day: "))
m1 = int(input("Month: "))
y1 = int(input("Year: "))
date1 = Date(d1, m1, y1)

print("\nEnter second date:")
d2 = int(input("Day: "))
m2 = int(input("Month: "))
y2 = int(input("Year: "))
date2 = Date(d2, m2, y2)

print(f"\nDate 1: {date1}")
print(f"Date 2: {date2}")

if date1 == date2:
    print("The two dates are equal.")
else:
    print("The two dates are not equal.")
