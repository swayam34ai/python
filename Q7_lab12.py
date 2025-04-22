class Weather:
    def __init__(self, parameters):
        self.parameters = parameters  # A list of weather parameters

    def __contains__(self, item):
        return item in self.parameters

    def __str__(self):
        return f"Weather Parameters: {', '.join(self.parameters)}"

params = ["Temperature", "Humidity", "Wind", "Rain", "Pressure"]
weather = Weather(params)

print(weather)

check = input("Enter a parameter to check (e.g., 'Humidity'): ")

if check in weather:
    print(f"'{check}' is in the weather data.")
else:
    print(f"'{check}' is NOT in the weather data.")