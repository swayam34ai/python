employees = [
    {"dept_no": 1, "roll_no": 73, "salary": 50000},
    {"dept_no": 1, "roll_no": 21, "salary": 45000},
    {"dept_no": 2, "roll_no": 34, "salary": 60000},
    {"dept_no": 2, "roll_no": 56, "salary": 75000},
    {"dept_no": 3, "roll_no": 12, "salary": 40000},
    {"dept_no": 3, "roll_no": 91, "salary": 30000},
]
dept_salaries = {}


for emp in employees:
    dept = emp["dept_no"]
    salary = emp["salary"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

for dept in dept_salaries:
    salaries = dept_salaries[dept]
    print("Dept", dept, "-> Min:", min(salaries), "Max:", max(salaries))