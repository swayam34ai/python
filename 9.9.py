def count_alpha_digits(text):
    result = {"alphabets": 0, "digits": 0}
    for char in text:
        if char.isalpha():
            result["alphabets"] += 1
        elif char.isdigit():
            result["digits"] += 1          
    return result
input_str = input("Enter a string: ")
counts = count_alpha_digits(input_str)
print("Count:", counts)