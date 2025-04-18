def generate_tuples(end):
    result = []
    for x in range(1, end + 1):
        result.append((x, x**2, x**3))
    return result
ending_value = int(input("Enter the ending value: "))
tuples_list = generate_tuples(ending_value)
for t in tuples_list:
    print(t)