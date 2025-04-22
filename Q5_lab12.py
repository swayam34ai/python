class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        # Convert excess seconds to minutes and excess minutes to hours
        total_seconds = self.to_seconds()
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def __add__(self, other):
        total = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total)

    def __sub__(self, other):
        total = self.to_seconds() - other.to_seconds()
        if total < 0:
            print("Resulting time is negative. Returning 00:00:00.")
            return Time()
        return Time.from_seconds(total)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

print("Enter first time:")
h1 = int(input("Hours: "))
m1 = int(input("Minutes: "))
s1 = int(input("Seconds: "))
t1 = Time(h1, m1, s1)

print("\nEnter second time:")
h2 = int(input("Hours: "))
m2 = int(input("Minutes: "))
s2 = int(input("Seconds: "))
