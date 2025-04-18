def remove_words_from_file(input_file, output_file):
    words_to_remove = [' a ', ' the ', ' an ']
    with open(input_file, 'r') as file:
        content = file.read()
    for word in words_to_remove:
        content = content.replace(word, ' ')
    with open(output_file, 'w') as output:
        output.write(content)
    print(f"Processed content written to {output_file}")
input_file = 'input.txt'
output_file = 'output.txt'
remove_words_from_file(input_file, output_file)