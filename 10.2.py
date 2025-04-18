def read_csv_to_dict(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = {}
    for line in lines[1:]:  
        parts = line.strip().split(',')
        rollno, name, marks1, marks2, marks3 = parts
        total = int(marks1) + int(marks2) + int(marks3)
        data[rollno] = {'name': name, 'marks1': int(marks1), 'marks2': int(marks2), 'marks3': int(marks3), 'total': total}
    return data
filename = 'students.csv'
data = read_csv_to_dict(filename)
print(data)