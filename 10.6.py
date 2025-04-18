def merge_alternatively(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    merged_lines = []
    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        if i < len(lines1):
            merged_lines.append(lines1[i].strip() + "\n")
        if i < len(lines2):
            merged_lines.append(lines2[i].strip() + "\n")
    with open(output_file, 'w') as output:
        output.writelines(merged_lines)
    print(f"Merged lines written to {output_file}")
file1 = 'file1.txt'
file2 = 'file2.txt'
output_file = 'merged.txt'
merge_alternatively(file1, file2, output_file)
