# List of Fahrenheit temperatures
fahrenheit_temps = [32, 68, 100, 212]

# Empty list to store Celsius temperatures
celsius_temps = []

# Loop to convert each Fahrenheit value to Celsius
for f in fahrenheit_temps:
    c = (f - 32) * 5 / 9  # Conversion formula
    celsius_temps.append(c)

# Print results
print("Fahrenheit:", fahrenheit_temps)
print("Celsius:", celsius_temps)