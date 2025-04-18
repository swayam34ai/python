def copy_and_uppercase(src_file, dest_file):
    with open(src_file, 'r') as source:
        content = source.read()
    content = content.upper()
    with open(dest_file, 'w') as dest:
        dest.write(content)
    print(f"Content copied and converted to uppercase in {dest_file}")
src_file = 'input.txt'
dest_file = 'output.txt'
copy_and_uppercase(src_file, dest_file)
