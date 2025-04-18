faculty_members = ["Dr. Smith", "Prof. Johnson", "Alice", "Bob", "Professor Green", "Dr. Taylor"]
filtered_names = list(filter(lambda name: len(name) > 8, faculty_members))
print("Faculty Members with names longer than 8 characters:", filtered_names)