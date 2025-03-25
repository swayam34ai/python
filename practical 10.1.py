data = [
    "Name,Age,City",  
    "swayam,18,surat",
    "Smith,24,australia"
]
filename = "people_data54.csv"
with open(filename, mode="w") as file:
    for row in data:
        file.write(row )
print(f"CSV file '{filename}' has been created successfully.")
