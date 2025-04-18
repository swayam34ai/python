def convert(text):
    words = text.split()
    unique_sorted_words = sorted(set(words))
    result = " ".join(unique_sorted_words)
    return result
input_str = input("Enter a string of words: ")
output_str = convert(input_str)
print("Processed string:", output_str)